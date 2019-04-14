
# Rest api documentation

    GET auth/log-in -> 200

        body:
        {
          UserId: ObjectId(name),
          password: Hash(password)
        }
        return:
        {
          "userId": ObjectId(rory),
          "serverTime": 3748329789090
        }

    print(response.userId, response.serverTime)

        PUT api/measurement/

            body: {}

            params: auth "string of hashed username and password separated with :"

            return:

         POST api/create_user

            body: {}

            params



