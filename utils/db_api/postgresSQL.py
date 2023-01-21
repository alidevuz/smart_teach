from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config



class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:

                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        full_name VARCHAR(355) NOT NULL,
        telegram_id BIGINT  NOT NULL UNIQUE  
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, telegram_id):
        sql = "INSERT INTO users (full_name, telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, full_name, telegram_id, fetchrow=True)

    async def select_users_one(self, telegram_id):
        sql = "SELECT * FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, id, telegram_id):
        sql = "UPDATE users SET id=$1 WHERE telegram_id=$2"
        return await self.execute(sql, id, telegram_id, execute=True)

    async def delete_users(self, telegram_id):
        sql = "DELETE FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def drop_users(self):
        await self.execute("DROP TABLE users", execute=True)






    async def create_table_login(self):
        sql = """
        CREATE TABLE IF NOT EXISTS login (
        ism VARCHAR(355) NOT NULL,
        familya VARCHAR(355) NOT NULL,
        fan1 VARCHAR(355) NOT NULL,
        fan2 VARCHAR(355) NOT NULL,
        fan3 VARCHAR(355) NOT NULL,
        payme1 VARCHAR(355) NOT NULL,
        payme2 VARCHAR(355) NOT NULL,
        payme3 VARCHAR(355) NOT NULL,
        filial VARCHAR(355) NOT NULL,
        guruh1 VARCHAR(355) NOT NULL,
        guruh2 VARCHAR(355) NOT NULL,
        guruh3 VARCHAR(355) NOT NULL,
        davomat1 VARCHAR(5000) NOT NULL,
        davomat2 VARCHAR(5000) NOT NULL,
        davomat3 VARCHAR(5000) NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_login(self, ism, familya, fan1, fan2, fan3, payme1, payme2, payme3, filial, guruh1, guruh2, guruh3, davomat1, davomat2, davomat3):
        sql = "INSERT INTO login (ism, familya, fan1, fan2, fan3, payme1, payme2, payme3, filial, guruh1, guruh2, guruh3, davomat1, davomat2, davomat3) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15) returning *"
        return await self.execute(sql, ism, familya, fan1, fan2, fan3, payme1, payme2, payme3, filial, guruh1, guruh2, guruh3, davomat1, davomat2, davomat3, fetchrow=True)


    async def select_login_one(self, user_id_1):
        sql = "SELECT * FROM login WHERE user_id_1=$1"
        return await self.execute(sql, user_id_1, fetchrow=True)

    async def select_login_two(self):
        sql = "SELECT ism, familya, fan1, fan2, fan3, payme1, payme2, payme3,filial, guruh1, guruh2, guruh3, davomat1, davomat2, davomat3 FROM login "
        return await self.execute(sql, fetch=True)

    async def select_login_search1(self, guruh1):
        sql = "SELECT ism, familya FROM login WHERE guruh1=$1"
        return await self.execute(sql, guruh1, fetch=True)
    async def select_login_search2(self, guruh2):
        sql = "SELECT ism, familya FROM login WHERE guruh2=$1"
        return await self.execute(sql, guruh2, fetch=True)
    async def select_login_search3(self, guruh3):
        sql = "SELECT ism, familya FROM login WHERE guruh3=$1"
        return await self.execute(sql, guruh3, fetch=True)

    async def count_login(self):
        sql = "SELECT COUNT(*) FROM login"
        return await self.execute(sql, fetchval=True)

    async def update_user_logins1(self, ism, familya, davomat1):
        sql = "UPDATE login SET davomat1=$3 WHERE ism=$1 and familya=$2"
        return await self.execute(sql, ism, familya, davomat1, execute=True)

    async def update_user_logins2(self, ism, familya, davomat2):
        sql = "UPDATE login SET davomat2=$3 WHERE ism=$1 and familya=$2"
        return await self.execute(sql, ism, familya, davomat2, execute=True)

    async def update_user_logins3(self, ism, familya, davomat3):
        sql = "UPDATE login SET davomat3=$3 WHERE ism=$1 and familya=$2"
        return await self.execute(sql, ism, familya, davomat3, execute=True)

    async def delete_login(self, telegram_id):
        sql = "DELETE FROM login WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def drop_login(self):
        await self.execute("DROP TABLE login", execute=True)




    async def create_panel_user(self):
        sql = """
        CREATE TABLE IF NOT EXISTS panel_users (
        namename VARCHAR(355) NOT NULL,
        full_name VARCHAR(355) NOT NULL,
        telegram_id BIGINT  NOT NULL UNIQUE  
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_panel_user(self, namename, full_name, telegram_id):
        sql = "INSERT INTO panel_users (namename, full_name, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, namename, full_name, telegram_id, fetchrow=True)

    async def select_panel_one(self, telegram_id):
        sql = "SELECT * FROM panel_users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetch=True)

    async def select_login_panel(self):
        sql = "SELECT * FROM panel_users "
        return await self.execute(sql, fetch=True)

    async def count_panel_users(self):
        sql = "SELECT COUNT(*) FROM panel_users"
        return await self.execute(sql, fetchval=True)

    async def update_user_panel(self, id, telegram_id):
        sql = "UPDATE panel_users SET id=$1 WHERE telegram_id=$2"
        return await self.execute(sql, id, telegram_id, execute=True)

    async def delete_panel_users(self, telegram_id):
        sql = "DELETE FROM panel_users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def drop_panel_users(self):
        await self.execute("DROP TABLE panel_users", execute=True)




    async def create_buxgalter(self):
        sql = """
        CREATE TABLE IF NOT EXISTS kassa (
        fan_nomi VARCHAR(355) NOT NULL,
        narxi VARCHAR(355) NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_kassa(self, fan_nomi, narxi):
        sql = "INSERT INTO kassa (fan_nomi, narxi) VALUES($1, $2) returning *"
        return await self.execute(sql, fan_nomi, narxi, fetchrow=True)

    async def select_kassa_one(self, fan_nomi):
        sql = "SELECT * FROM kassa WHERE fan_nomi=$1"
        return await self.execute(sql, fan_nomi, fetch=True)

    async def select_kassa_panel(self):
        sql = "SELECT telegram_id FROM kassa "
        return await self.execute(sql, fetch=True)

    async def count_panel_kassa(self):
        sql = "SELECT COUNT(*) FROM kassa"
        return await self.execute(sql, fetchval=True)

    async def update_user_kassa(self, id, telegram_id):
        sql = "UPDATE kassa SET id=$1 WHERE telegram_id=$2"
        return await self.execute(sql, id, telegram_id, execute=True)

    async def delete_panel_kassa(self, telegram_id):
        sql = "DELETE FROM kassa WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def drop_panel_kassa(self):
        await self.execute("DROP TABLE kassa", execute=True)

    async def create_teacher_login(self):
        sql = """
           CREATE TABLE IF NOT EXISTS teachr (
           ism VARCHAR(355) NOT NULL,
           familya VARCHAR(355) NOT NULL,
           guruhi0 VARCHAR(355) NOT NULL,
           guruhi1 VARCHAR(355) NOT NULL,
           guruhi2 VARCHAR(355) NOT NULL,
           guruhi3 VARCHAR(355) NOT NULL,
           guruhi4 VARCHAR(355) NOT NULL,
           guruhi5 VARCHAR(355) NOT NULL,
           guruhi6 VARCHAR(355) NOT NULL,
           guruhi7 VARCHAR(355) NOT NULL,
           home0 VARCHAR(5000) NOT NULL,
           home1 VARCHAR(5000) NOT NULL,
           home2 VARCHAR(5000) NOT NULL,
           home3 VARCHAR(5000) NOT NULL,
           home4 VARCHAR(5000) NOT NULL,
           home5 VARCHAR(5000) NOT NULL,
           home6 VARCHAR(5000) NOT NULL,
           home7 VARCHAR(5000) NOT NULL,
           id1 VARCHAR(300) NOT NULL,
           id2 VARCHAR(300) NOT NULL,
           id3 VARCHAR(300) NOT NULL, 
           fan_edu VARCHAR(300) NOT NULL
           );
           """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_teacher(self, ism, familya, guruhi0, guruhi1, guruhi2, guruhi3, guruhi4, guruhi5, guruhi6, guruhi7, home0, home1, home2, home3, home4, home5, home6, home7, id1, id2, id3, fan_edu):
        sql = "INSERT INTO teachr (ism, familya, guruhi0, guruhi1, guruhi2, guruhi3, guruhi4, guruhi5, guruhi6, guruhi7, home0, home1, home2, home3, home4, home5, home6, home7, id1, id2, id3, fan_edu) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22) returning *"
        return await self.execute(sql, ism, familya, guruhi0, guruhi1, guruhi2, guruhi3, guruhi4, guruhi5, guruhi6, guruhi7, home0, home1, home2, home3, home4, home5, home6, home7, id1, id2, id3, fan_edu, fetchrow=True)

    async def select_teacher_one(self, user_id_1):
        sql = "SELECT * FROM teachr WHERE user_id_1=$1"
        return await self.execute(sql, user_id_1, fetchrow=True)

    async def select_teacher_two(self):
        sql = "SELECT ism, familya, id1, id2, id3 FROM teachr "
        return await self.execute(sql, fetch=True)

    async def select_teachers_search_fan(self):
        sql = "SELECT fan_edu, guruhi0, guruhi1, guruhi2, guruhi3, guruhi4, guruhi5, guruhi6, guruhi7 FROM teachr "
        return await self.execute(sql, fetch=True)

    async def select_teachers_search(self, ism, familya):
        sql = "SELECT guruhi0, guruhi1, guruhi2, guruhi3, guruhi4, guruhi5, guruhi6, guruhi7 FROM teachr WHERE ism=$1 and familya=$2"
        return await self.execute(sql, ism, familya, fetch=True)

    async def count_teacher(self):
        sql = "SELECT COUNT(*) FROM teachr"
        return await self.execute(sql, fetchval=True)

    async def update_teacher_login1(self, ism, familya, id1):
        sql = "UPDATE teachr SET id1=$3 WHERE ism=$1 and familya=$2"
        return await self.execute(sql, ism, familya, id1, execute=True)

    async def delete_teacher(self, telegram_id):
        sql = "DELETE FROM teachr WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def drop_teacher(self):
        await self.execute("DROP TABLE teachr", execute=True)



    async def create_panel_teachers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS panel_teachers (
        namename3 VARCHAR(355) NOT NULL,
        full_name3 VARCHAR(355) NOT NULL,
        telegram_id3 BIGINT  NOT NULL   
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_panel_teacher(self, namename3, full_name3, telegram_id3):
        sql = "INSERT INTO panel_teachers (namename3, full_name3, telegram_id3) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, namename3, full_name3, telegram_id3, fetchrow=True)

    async def select_panel_teacher(self, telegram_id3):
        sql = "SELECT * FROM panel_teachers WHERE telegram_id3=$1"
        return await self.execute(sql, telegram_id3, fetch=True)

    async def select_login_teacher(self):
        sql = "SELECT telegram_id3 FROM panel_teachers "
        return await self.execute(sql, fetch=True)

    async def count_panel_teacher(self):
        sql = "SELECT COUNT(*) FROM panel_teachers"
        return await self.execute(sql, fetchval=True)

    async def update_user_teacher(self, id, telegram_id):
        sql = "UPDATE panel_teachers SET id=$1 WHERE telegram_id=$2"
        return await self.execute(sql, id, telegram_id, execute=True)

    async def delete_panel_teacher(self, telegram_id3):
        sql = "DELETE FROM panel_teachers WHERE telegram_id3=$1"
        return await self.execute(sql, telegram_id3, fetchrow=True)

    async def drop_panel_users3(self):
        await self.execute("DROP TABLE panel_teachers", execute=True)
