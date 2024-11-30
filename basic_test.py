import openai
from colorama import Fore, Style
from tqdm import tqdm

# הודעה ראשונית
print(Fore.GREEN + "All libraries imported successfully!" + Style.RESET_ALL)

# סימולציה של סרגל התקדמות
for i in tqdm(range(10), desc="Testing tqdm"):
    pass
