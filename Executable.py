# Author: Mortey Emmanuel Kwesi
# email: exmortey@gmail.com
# The Scoring Module will use up to eight parameters (with percentages):
# Age (6%) - 51
# Education (7%) - 68
# Yearly Income (11%) - 93.5
# Number of Dependents (85) - 68
# Payment History (27%) - 229.5
# Credit Utilisation (20%) - 170
# Length of Credit History (12%) - 102
# New Credit (8%) - 68
# *Twitter(5%) - 42.5 (Only computed if the applicant has a Twitter Account)

credit_score = 0

print("**************** CREDIT SCORING MODULE ****************")
print('''

Enter the number beside the option to select it
Otherwise follow specified instructions
All monetary values are in Ghana Cedis
''')

while True:
    try:
        age = int(input('Enter age of applicant: '))
        if age < 22:
            credit_score = credit_score + 10
        elif 22 <= age < 26:
            credit_score = credit_score + 22
        elif 26 <= age < 37:
            credit_score = credit_score + 35
        elif 37 <= age < 42:
            credit_score = credit_score + 41
        elif age > 42:
            credit_score = credit_score + 51

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break
print(credit_score)

while True:
    try:
        education_level = int(input('''
Select your Level of Education:
1. None
2. Primary
3. JHS
4. SHS
5. First Degree / Diploma
6. Second Degree and Above
        '''))
        if education_level > 6 or education_level < 1:
            raise ValueError

        if education_level == 1:
            credit_score = credit_score + 10
        elif education_level == 2:
            credit_score = credit_score + 18
        elif education_level == 3:
            credit_score = credit_score + 25
        elif education_level == 4:
            credit_score = credit_score + 45
        elif education_level == 5:
            credit_score = credit_score + 55
        elif education_level == 6:
            credit_score = credit_score + 68

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break
print(credit_score)

income_value = 0
while True:
    try:
        monthly_income = int(input('''
Do you have a stable income:
1. Yes 
2. No
        '''))
        if monthly_income > 2 or monthly_income < 1:
            raise ValueError

        if monthly_income == 1:
            while True:
                try:
                    income_value = int(input('''
Select the range of your yearly income:
1. Less than GH₵ 10, 000
2. Between GH₵ 10, 000 and GH₵ 17, 000
3. Between GH₵ 17, 000 and GH₵ 28, 000
4. Between GH₵ 28, 000 and GH₵ 36, 000
5. Above GH₵ 36, 000
        '''))
                    if income_value < 1:
                        raise ValueError

                    if income_value == 1:
                        credit_score = credit_score + 33.5
                    elif income_value == 2:
                        credit_score = credit_score + 48.5
                    elif income_value == 3:
                        credit_score = credit_score + 63.5
                    elif income_value == 4:
                        credit_score = credit_score + 78.5
                    elif income_value == 5:
                        credit_score = credit_score + 93.5

                except ValueError as err:
                    print("Your input is invalid\nTry again")
                else:
                    break

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break

while True:
    try:
        num_of_dependents = int(input("Enter the number of dependents you have:\n Excluding yourself "))
        if num_of_dependents < 0:
            raise ValueError

        if num_of_dependents == 0:
            credit_score = credit_score + 68
        if num_of_dependents == 1:
            credit_score = credit_score + 34
        elif num_of_dependents == 2:
            credit_score = credit_score + 17
        elif num_of_dependents == 3:
            credit_score = credit_score + 9
        elif num_of_dependents == 4:
            credit_score = credit_score + 5
        elif num_of_dependents >= 5:
            credit_score = credit_score + 3

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break

while True:
    try:
        num_of_accounts = int(input('Enter the number of credit accounts or loans you have: '))
        if num_of_accounts < 1:
            raise ValueError

    except ValueError as err:
        print("Your input is invalid\nYou need to hava at least one credit account or loan\nTry again")
    else:
        break

print(num_of_accounts)
account_lives = 0
amount_owed, amount_paid, credit_utilisation, total_credit_utilisation, loan_delinquency, total_loan_delinquency = 0, 0, 0, 0, 0, 0
i = 0
for i in range(num_of_accounts):
    print("\nDetails of Account", i + 1, ':')
    while True:
        try:
            print('How long have you had Account(Credit Account or Loan )', i + 1, ':')
            account_life = int(input('Enter in year(s): '))

            if account_life <= 0:
                raise ValueError

            while True:
                try:
                    print('''
Select the type of account
1. Credit Account
2. Loan
                    ''')
                    choice = int(input('Input here: '))

                    if choice < 1 or choice > 2:
                        raise ValueError

                except ValueError as err:
                    print("Your input is invalid\nTry again")
                else:
                    break

            while True:
                try:
                    if choice == 1:
                        amount_owed = int(input("What's the limit of the credit account: "))
                        amount_paid = int(input("How much of the credit was used: "))
                        credit_utilisation = (amount_paid / amount_owed) * 100
                    else:
                        amount_owed = int(input("How much is the total loan: "))
                        amount_paid = int(input("How much of the loan has been paid: "))
                        credit_utilisation = (amount_paid / amount_owed) * 100

                    if amount_owed < 0 or amount_paid < 0 or amount_paid > amount_owed:
                        raise ValueError

                    while True:
                        try:
                            print('''
                    Have you ever been delinquent on repayment for this account
                    Select 1 if you have never
                    1. 0
                    2. Over 30 days 
                    3. Over 60 days
                    4. Over 90 days
                                                ''')
                            choice_del = int(input('Enter your choice: '))

                            if choice_del < 1 or choice_del > 4:
                                raise ValueError

                            if choice_del == 1:
                                loan_delinquency = 0
                            elif choice_del == 2:
                                loan_delinquency = 46
                            elif choice_del == 3:
                                loan_delinquency = 58
                            elif loan_delinquency == 4:
                                loan_delinquency = 69

                        except ValueError as err:
                            print("Your input is invalid\nTry again")
                        else:
                            break

                except ValueError as err:
                    print('''
            Invalid input
            Make sure:
            Total Loan/ Limit of Credit Account is greater than zero
            Loan Paid/ Credit used is greater than zero and less than Total Loan/ Limit of Credit Account
            Try again
                    ''')
                else:
                    break

            account_lives = account_lives + account_life
            total_credit_utilisation = total_credit_utilisation + credit_utilisation
            total_loan_delinquency = total_loan_delinquency + loan_delinquency

        except ValueError as err:
            print('''
            Invalid input
            Make sure:
            Account Life is greater than zero
        ''')
        else:
            break

avg_account_lives = account_lives / num_of_accounts
avg_credit_utilisation = total_credit_utilisation / num_of_accounts

if avg_account_lives == 1:
    credit_score = credit_score + 10
elif avg_account_lives == 2:
    credit_score = credit_score + 24
elif avg_account_lives == 3:
    credit_score = credit_score + 35
elif avg_account_lives == 4:
    credit_score = credit_score + 51
elif avg_account_lives == 5:
    credit_score = credit_score + 65
elif avg_account_lives == 6:
    credit_score = credit_score + 85
elif avg_account_lives >= 7:
    credit_score = credit_score + 102

credit_score = credit_score + 170
if 50 < avg_credit_utilisation <= 60:
    credit_score = credit_score - 30
elif 60 < avg_credit_utilisation <= 70:
    credit_score = credit_score - 60
elif 70 < avg_credit_utilisation <= 80:
    credit_score = credit_score - 90
elif 70 < avg_credit_utilisation:
    credit_score = credit_score - 120

while True:
    try:
        print('''
Have you ever been delinquent on repayment for a loan or credit payment in the past
Pick an estimate of the total amount of time
Select 1 if you have never
1. 0
2. Over 30 days
3. Over 60 days
4. Over 90 days
5. Over 110 days
                            ''')
        choice_del = int(input('Enter your choice: '))

        if choice_del < 1 or choice_del > 5:
            raise ValueError

        if choice_del == 1:
            loan_delinquency2 = 0
        elif choice_del == 2:
            loan_delinquency2 = 46
        elif choice_del == 3:
            loan_delinquency2 = 58
        elif choice_del == 4:
            loan_delinquency2 = 69
        elif choice_del == 5:
            loan_delinquency2 = 110

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break

total_loan_delinquency = total_loan_delinquency + loan_delinquency2
net_delinquency = 229.5 - total_loan_delinquency
if net_delinquency < 0:
    net_delinquency = 0
credit_score = credit_score + net_delinquency

while True:
    try:
        print('''
How many credit accounts or loans have you opened within the last 6 months
1. 0
2. 1
3. 2
4. 3
5. 4 
6. 5 and above
                                    ''')
        new_credit = int(input('Select your choice '))

        print(new_credit)
        if new_credit < 0 or new_credit > 6:
            raise ValueError

        if new_credit == 1:
            credit_score = credit_score + 68
        elif new_credit == 2:
            credit_score = credit_score + 58
        elif new_credit == 3:
            credit_score = credit_score + 48
        elif new_credit == 4:
            credit_score = credit_score + 38
        elif new_credit == 5:
            credit_score = credit_score + 28
        elif new_credit > 5:
            credit_score = credit_score + 18

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break

import Twitter_Analysis

tw_username = ''
print(tw_username)
text_tweets = Twitter_Analysis.get_tweets(tw_username)
cleaned_text = Twitter_Analysis.clean_tweets(text_tweets)
sentiment_value = Twitter_Analysis.sentiment_analyze(cleaned_text)

if sentiment_value > 0:
    credit_score = 0.95 * credit_score
    credit_score = credit_score + sentiment_value
else:
    pass

print("Calculating Credit Score...........")
print("\nHere's your Credit Score: ", credit_score)
if credit_score < 580:
    print('Grade: Poor')
elif 580 < credit_score <= 670:
    print('Grade: Fair')
elif 670 < credit_score <= 740:
    print('Grade: Good')
elif 740 < credit_score <= 800:
    print('Grade: Very Good')
elif credit_score > 800:
    print('Grade: Excellent')
