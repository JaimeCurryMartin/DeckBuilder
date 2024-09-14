import subprocess

def run_script(script_name):
    try:
        result = subprocess.run(['python3', script_name], check=True, capture_output=True, text=True)
        print(f"Output of {script_name}:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}:")
        print(e.stderr)

if __name__ == "__main__":
    scripts = [
        '/Users/administrador/Documents/DeckBuilder/find_cards/find_cards.py', 
        '/Users/administrador/Documents/DeckBuilder/clear_data/clear_data.py',  
        '/Users/administrador/Documents/DeckBuilder/buscar_patron/advice_deck.py'  
    ]
    
    for script in scripts:
        run_script(script)
