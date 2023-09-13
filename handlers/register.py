from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from states import RegisterStates
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import get_inline_markup
from keyboards.default import get_choice_markup, get_phone_markup, get_confirm_markup, register_markup
from extra.db import add_player_to_db

router = Router()

@router.message(F.text == "👤 Ro'yxatdan o'tish")
async def start_register(message: types.Message, state: FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun Ism Familiya Sharifingizni kiriting\n\n<i>Na'muna: Abdullayev Abdulla Abdullayevich</i>", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterStates.fio)


@router.message(RegisterStates.fio, F.text)
async def get_fio(message: types.Message, state: FSMContext):
    await state.set_data({"fio": message.text})
    await message.answer("<b>Yoshingizni raqamlarda kiriting - bu sizning tanlovdagi ishtirokingiz uchun muhim</b>\n\n<i>Na'muna: 18</i>")
    await state.set_state(RegisterStates.age)


@router.message(RegisterStates.age, F.text.isdigit())
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data({"age": int(message.text)})
    await message.answer("<b>Qatnashmoqchi bo'lgan tanlovingizni belgilang</b>\n\n<i>* Eslatma: Tanlovlarning faqat bittasida ishtirok etish mumkin!</i>", reply_markup=get_inline_markup())
    await state.set_state(RegisterStates.choice)

@router.callback_query(RegisterStates.choice, F.data)
async def get_choice_data(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"choice": call.data})
    await call.message.delete()
    await call.message.answer("<b>Hozirgi ijtimoiy holatingizni belgilang</b>", reply_markup=get_choice_markup())
    await state.set_state(RegisterStates.status)


@router.message(RegisterStates.status, F.text.in_(["O'quvchi", "Talaba", "Uyushmagan yosh"]))
async def get_status(message: types.Message, state: FSMContext):
    await state.update_data({"status": message.text})
    await message.answer("<b>Telefon raqamingizni yuboring yoki ro'yhatdan o'tmoqchi bo'lgan raqamingizni kiriting</b>\n\n<i>Na'muna: +998912345678</i>", reply_markup=get_phone_markup())
    await state.set_state(RegisterStates.phone_number)


@router.message(RegisterStates.phone_number, F.contact)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data({"phone_number": message.contact.phone_number})
    user_data = await state.get_data()
    msg_text = f"<b>Ma'lumotlaringiz:</b>\n\nFIO: {user_data.get('fio')}\nYosh: {user_data.get('age')}\nIjtimoiy holati: {user_data.get('status')}\nTanlov: {user_data.get('choice')}\nTelefon raqami: {user_data.get('phone_number')}"
    await message.answer(msg_text, reply_markup=get_confirm_markup())
    await state.set_state(RegisterStates.confirm)


@router.message(RegisterStates.confirm, F.text == "✅ Ha")
async def confirm(message: types.Message, state: FSMContext):
    await message.answer("✅ Ro'yhatdan o'tish muvaffaqiyali amalga oshirildi!", reply_markup=register_markup())
    user_data = await state.get_data()
    add_player_to_db(fio=user_data.get('fio'), age=user_data.get('age'), status=user_data.get('status'), choice=user_data.get('choice'), phone_number=user_data.get('phone_number'))
    await state.clear()


@router.message(RegisterStates.confirm, F.text == "❌ Yo'q")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("❌ Ro'yhatdan o'tish bekor qilindi", reply_markup=register_markup())
    await state.clear()
