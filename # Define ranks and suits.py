import random
# Define ranks and suits
ranks = list(range(1, 14))  # 1 to 13 (Ace to King)
suits = ['heart', 'diamond', 'club', 'spade']

# Create a list of tuples for each card
deck = [(rank, suit) for suit in suits for rank in ranks]

def shuffle(deck):
    n=[]
    s=[]
    e=[]
    w=[]
    for i in range(13):
        card = random.choice(deck)
        n.append(card)
        deck.remove(card)
    for i in range(13):
        card = random.choice(deck)
        s.append(card)
        deck.remove(card)
    for i in range(13):
        card = random.choice(deck)
        e.append(card)
        deck.remove(card)
    for i in range(13):
        card = random.choice(deck)
        w.append(card)
        deck.remove(card)
    print(n)
    print(s)
    print(e)
    print(w)
    print(len(deck))
shuffle(deck)


import tkinter as tk
import random
from PIL import Image, ImageTk  # Requires Pillow library for image handling

class CardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Shuffler Interface")
        self.root.geometry("1000x1500")
        
        # Define ranks and suits
        self.ranks = list(range(1, 14))  # 1 to 13 (Ace to King)
        self.suits = ['heart', 'diamond', 'club', 'spade']
        self.deck = self.create_deck()
        self.hands = [[], [], [], []]  # 4 empty sections for cards
        
        # Create sections for the hands
        self.hand_frames = [tk.Frame(root, relief=tk.RAISED, borderwidth=2) for _ in range(4)]
        for i, frame in enumerate(self.hand_frames):
            frame.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            tk.Label(frame, text=f"Hand {i + 1}", font=("Helvetica", 14)).pack(pady=5)

        # Create buttons
        self.show_button = tk.Button(root, text="Show Cards", command=self.show_cards)
        self.show_button.grid(row=1, column=0, padx=10, pady=10)

        self.shuffle_button = tk.Button(root, text="Reshuffle Cards", command=self.reshuffle_cards)
        self.shuffle_button.grid(row=1, column=1, padx=10, pady=10)

        self.empty_button = tk.Button(root, text="Show Empty Sections", command=self.show_empty_sections)
        self.empty_button.grid(row=1, column=2, padx=10, pady=10)

    def create_deck(self):
        """Creates a standard deck of cards."""
        return [(rank, suit) for suit in self.suits for rank in self.ranks]

    def show_cards(self):
        """Displays card images in each hand."""
        for i in range(4):
            # Clear the current hand display
            for widget in self.hand_frames[i].winfo_children():
                if widget.winfo_name() != 'label':  # Keep the section label
                    widget.destroy()

            # Show the images of the cards in the hand
            for card in self.hands[i]:
                rank, suit = card
                image_path = f"{rank}_{suit}.png"  # Update the image path as needed
                image = Image.open(image_path)
                image = image.resize((50,60), Image.LANCZOS)  # Resize image
                photo = ImageTk.PhotoImage(image)
                
                card_label = tk.Label(self.hand_frames[i], image=photo)
                card_label.image = photo  # Keep a reference to avoid garbage collection
                card_label.pack()

    def reshuffle_cards(self):
        """Reshuffles the deck and deals new cards to each hand."""
        self.deck = self.create_deck()  # Reset the deck
        random.shuffle(self.deck)  # Shuffle the deck

        # Clear hands and deal new cards
        self.hands = [self.deck[i * 13:(i + 1) * 13] for i in range(4)]
        print(self.hands)

    def show_empty_sections(self):
        """Clears all hands to show they are empty."""
        self.hands = [[], [], [], []]
        self.show_cards()  # Call show_cards to update the display

if __name__ == "__main__":
    root = tk.Tk()
    app = CardGame(root)
    root.mainloop()








