import gitlab
import re

# 공개 리소스에 대한 익명의 읽기 전용 액세스(자체 호스팅 GitLab 인스턴스)

# gitlab url 및 token 입력
gl = gitlab.Gitlab(domain, private_token="token")


users = gl.users.list(iterator=True)
for user in users:
        ## 문자열 자르기 
        email = user.email
        secondary_email = email.replace(email[email.find('.'):email.find('@')], "");
        secondary_email = secondary_email.replace("mergerity", "arbeon")
        print("primary:" + email + ", Secondary:" + secondary_email)
        
        if(email != secondary_email):
            string_secondary_email = secondary_email
            secondary_email = user.emails.create({'email': string_secondary_email, 'skip_confirmation': True})
            # email = user.emails.get(email)
            # user.email = user.email.replace("mergerity.com", "arbeon.com")
            
            user.email = string_secondary_email
            user.save()
            
            emails = user.emails.list(iterator=True)
            for email in emails:
                if(email != secondary_email):
                    email.delete()
