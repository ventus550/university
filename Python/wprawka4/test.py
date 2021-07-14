with open('users.db', encoding = 'utf-8') as f:
        for x in f:
            print(x.split(sep = ':'))
        
            
