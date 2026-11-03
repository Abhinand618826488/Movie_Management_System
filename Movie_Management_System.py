import mysql.connector

class movie:
    def get_connected(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="abhi",
                password="abhinad",
                database="movie_db"
            )
            return self.connection
        except Exception as e:
            print(e)
            return None

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="""
               select * from movie where id=%s
            """
            values=id,
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)
            return None
#GET
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="""select * from movie"""
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)

        except Exception as e:
            print(e)
#INSERT
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""
               insert into movie(movie_name,director,language,genre,rating)
               values(%s,%s,%s,%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()

            print("Movie Added Successfully")

        except Exception as e:
            print(e)
#RETRIEVE
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record is not None:
                print(record)
            else:
                print("Movie does not exist")
        except Exception as e:
            print(e)
#DELETE
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            if record is not None:
                self.cursor=self.connection.cursor()

                query="""
                  delete from movie where id=%s
                """
                values=[id,]
                self.cursor.execute(query,values)
                self.connection.commit()
                print("deleted Successfully")
            else:
                print("Movie does not exist")
        except Exception as e:
            print(e)
#PUT
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record is not None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k + "=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update movie set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Updated Successfully")
            else:
                print("Movie does not exist")
        except Exception as e:
            print(e)







connection_instance=movie()
print(connection_instance.get_connected())
#
# connection_instance.post(
#     movie_name="Drishyam",
#     director="Jeethu Joseph",
#     language="Malayalam",
#     genre="Thriller",
#     rating=9.0
# )
#
# connection_instance.post(
#     movie_name="Premam",
#     director="Alphonse Puthren",
#     language="Malayalam",
#     genre="Romance",
#     rating=8.5
# )
#
# connection_instance.post(
#     movie_name="Manjummel Boys",
#     director="Chidambaram",
#     language="Malayalam",
#     genre="Adventure",
#     rating=8.7
# )
# connection_instance.post(
#     movie_name="Interstellar",
#     director="Christopher Nolan",
#     language="English",
#     genre="Sci-Fi",
#     rating=8.7
# )
# connection_instance.post(
#     movie_name="3 Idiots",
#     director="Rajkumar Hirani",
#     language="Hindi",
#     genre="Comedy",
#     rating=8.4
# )
# connection_instance.retrieve(id=2)
# connection_instance.delete(id=5)
connection_instance.put(id=1,rating=9.5)

