def main():
    import random
    quick_picks =[]
    row = int(input('How many quick picks? '))
    for times in range(0,row):
        for i in range(0,6):
            quick_pick = random.randint(1,45)
            quick_picks.append(quick_pick)
            new_quick_picks = [str(a) for a in quick_picks]
        print(', '.join(new_quick_picks))
        quick_picks = []
    print()
main()