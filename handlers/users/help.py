from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    # a = 0
    # jad = ['rus tili','kimyo','matematika','kores tili','fizika','tarix','biologiya','geografiya','ingiliz tili','ona tili','mental arifmetika','prezident maktabiga tayyorlov']
    # for i in jad:
    #     a += 1
    #     await db.add_kassa(fan_nomi=i,
    #                        narxi="150000")


        l = 0
        for i in range(430):
            l += 1
            await db.add_login(ism=f"Ali{l}",
                       familya=f"Dali{l}",
                       fan1="ingiliz tili",
                       fan2="ona tili",
                       fan3="matematika",
                       payme1="24.04.2022",
                       payme2="12.09.2022",
                       payme3="03.03.1998",
                       filial="SH",
                       guruh1="G8",
                       guruh2="B3",
                       guruh3="M4",
                       davomat1="12.03.2022/23.11.2023",
                       davomat2="15.03.2022/13.11.2023",
                       davomat3="18.03.2022/20.11.2023")
            # await db.add_teacher(ism=F"sh{l}",
            #                      familya=f"a{l}",
            #                      guruhi0=f"G{l+2}",
            #                      guruhi1=f"G{l+3}",
            #                      guruhi2=f"G{l+4}",
            #                      guruhi3=f"G{l+5}",
            #                      guruhi4=f"G{l+6}",
            #                      guruhi5=f"G{l+7}",
            #                      guruhi6="0",
            #                      guruhi7=f"G-{l}",
            #                      home0="sssssssssssssssssssssssssssssssssssssss",
            #                      home1="sssssssssssssssssssssssssssssssssssssss",
            #                      home2="sssssssssssssssssssssssssssssssssssssss",
            #                      home3="sssssssssssssssssssssssssssssssssssssss",
            #                      home4="0",
            #                      home5="sssssssssssssssssssssssssssssssssssssss",
            #                      home6="0",
            #                      home7="sssssssssssssssssssssssssssssssssssssss",
            #                      id1="0",
            #                      id2="0",
            #                      id3=f"{message.from_user.id}",
            #                      fan_edu="matematika")


