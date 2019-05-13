        print(str(mention.id) + ' - ' + mention.full_text)
                last_seen_id = mention.id
                store_last_seen_id(last_seen_id, FILE_NAME)
                if "#helloworld" in mention.full_text.lower():
                        print('found Helloworld')
                        print('responding back')
                        api.update_status('@' + mention.user.screen_name +
                                '#HelloWorld back To You!!', mention.id)