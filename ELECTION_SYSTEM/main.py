from input import InputClass
from election_system import ElectionSystem


if __name__ == "__main__":

    inp_obj = InputClass("C:\\users\\rshaikh\\Pictures\\Test\\SSD\\ELECTION_SYSTEM\\input.txt")
    inp_obj.process_input()

    election_obj = ElectionSystem(inp_obj)

    while True:

        ch = int(input("Enter Choices: 1.PM \n 2. Consistuency:Party wise share \\\
              \n 3. party wise vote share \n 4. Given candidate:show his vote share \\\
              \n 5. Display Top 5 candidates in terms of vote share \\\
              \n 6. Display Top3 party by vote_share \n 7.exit"))

        if ch == 1:
            print(election_obj.calculate_pm())
        elif ch == 2:
            cn = input("Enter Consistuency:")
            print(election_obj.get_partywise_vote_cn(cn))
        elif ch == 3:
            print(election_obj.get_partywise_vote_share())
        elif ch == 4:
            cn = input("Enter candidate:")
            print(election_obj.get_voteshare_candidate(cn))
        elif ch == 5:
            print(election_obj.display_top_vote_share('candidate', 5))
        elif ch == 6:
            print(election_obj.display_top_vote_share('party', 3))
        else:
            break


