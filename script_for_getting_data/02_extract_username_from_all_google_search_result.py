username_list = []

def extract_github_username_from_file(filename, username_list):

    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        for word in line.strip().split(' '):
            if 'github.com/' in word:
            
                # Clean Data
            
                # Remove GitHub domain name
                username = word.split('github.com/')[1]
                
                # Remove Full stop
                username = username.split('.')[0]

                # Remove Tilde
                username = username.replace('~','')
                
                # Remove Comma
                username = username.split(',')[0]
                
                # Remove Quotation Marks
                username = username.replace('"', '')
                username = username.replace("'", '')
                    
                # Remove parameters
                username = username.split('?')[0]
                
                # Handle Repository with Extracting forward slash
                username = username.split('/')[0]
                
                # Remove Bracket
                username = username.replace(')', '')
                username = username.replace(']', '')

                # Handle Incomplete Username
                if '…' in username:
                    pass
                else:
                    if username:                        
                        username_list.append(username)
    file.close()
    
extract_github_username_from_file("all.txt", username_list)

print('Remove Duplicates')
print("before: ", len(username_list))
username_list = list(set(username_list))
print("before: ", len(username_list))
 
# Write Result to File
output_file = open('extracted_github_username.txt', 'w')
result_list = [username + "\n" for username in username_list]
output_file.writelines(result_list)
output_file.close()
