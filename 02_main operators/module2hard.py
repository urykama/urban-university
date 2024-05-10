def password_search(n):
    result = []
    for i in range(1, (n + 1) // 2):
        start = i + 1
        while start < n:
            if n % (i + start) == 0:
                result.extend([str(i), str(start)])
            start += 1
    return ''.join(result)


test_date = {3: '12',
             4: '13',
             5: '1423',
             6: '121524',
             7: '162534',
             8: '13172635',
             9: '1218273645',
             10: '141923283746',
             11: '11029384756',
             12: '12131511124210394857',
             13: '112211310495867',
             14: '1611325212343114105968',
             15: '1214114232133124115106978',
             16: '1317115262143531341251161079',
             17: '11621531441351261171089',
             18: '12151811724272163631545414513612711810',
             19: '118217316415514613712811910',
             20: '13141911923282183731746416515614713812911'}

its_ok = True
for key, value in test_date.items():
    if str(value) != password_search(key):
        print('ERROR with key:', key)
        print('\t Right password \t', value)
        print('\t Input password \t', password_search(key))
        its_ok = False

if its_ok:
    print('OK! All password is right')
