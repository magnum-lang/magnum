import magnum
import colorama
import time

version: str = '0.1'
colorama.init(True)

print(f"Magnum version {version}")

while True:
    print(
        f'[{colorama.Fore.GREEN + time.strftime("%I:%M %p") + colorama.Fore.WHITE}]{colorama.Fore.BLUE}>>>{colorama.Fore.LIGHTBLACK_EX} ',
        end='')
    text = input()

    if text == 'exit':
        exit(0)

    result, error = magnum.run('<stdin>', text)

    if error:
        print(colorama.Fore.RED + str(error))
    elif result != []:
        print(result)
    else:
        pass
