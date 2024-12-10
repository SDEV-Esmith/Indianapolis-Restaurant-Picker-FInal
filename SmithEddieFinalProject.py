"""
Author: Eddie Smith
Date:12/10/24
Program: Indianpolis Restaurant Picker
Version: 3.0
"""
import tkinter as tk
import random as rd

class ChooseRestaurant:
    """Class for fetching/returning a random restaurant from chosen price tier"""
    def __init__(self, low, medium, high):
        """Initialize parameters for fetching from price tier"""
        self.low = low
        self.medium = medium
        self.high = high

    #Get random restaurant
    def low_price_chosen(self):
        """Get random choice from low price dictionary"""
        random_rest = rd.choice(list(self.low.keys()))
        return random_rest
    def medium_price_chosen(self):
        """Get random choice from medium price dictionary"""
        random_rest = rd.choice(list(self.medium.keys()))
        return random_rest
    def high_price_chosen(self):
        """Get random choice from high price dictionary"""
        random_rest = rd.choice(list(self.high.keys()))
        return random_rest

class FetchImage:
    """Handles fetching/returning images from specified tier"""
    def __init__(self, random_rest, low, medium, high):
        """Initialize random restaurant and price tiers for getting image from dictionary"""
        self.random_rest = random_rest
        self.low = low
        self.medium = medium
        self.high = high


    def fetch_low_image(self, random_rest):
        """Get image from low price list"""
        chosen_image = self.low.get(random_rest)
        return chosen_image


    def fetch_medium_image(self, random_rest):
        """Get image from medium price list"""
        chosen_image = self.medium.get(random_rest)
        return chosen_image


    def fetch_high_image(self, random_rest):
        """Get image from high price list"""
        chosen_image = self.high.get(random_rest)
        return chosen_image

class Application:
    """Class for handling our application"""
    #Initialize root, images, dictionaries, background image, and welcome screen
    def __init__(self, root):
        self.root = root
        self.images = self.initialize_images()
        self.low_price, self.medium_price, self.high_price = self.initialize_dict(self.images)
        self.background_image = tk.PhotoImage(file = "Restaurant Images/background_image.png")
        self.background_label = tk.Label(root, image = self.background_image)
        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.root.background_image = self.background_image
        self.welcome_screen()
        self.last_restaurant = None

    #Initialize images
    def initialize_images(self):
        """Read in all images"""
        #Initialize empty dictionary
        images = {}
        try:
                #Key is "restaurant_image" and value is the image read in
                images["great_divide_image"] = tk.PhotoImage(file = "Restaurant images/great_divide_image.png")
                images["john_stew_image"] = tk.PhotoImage(file = "Restaurant images/john_stew_image.png")
                images["la_eskina_image"] = tk.PhotoImage(file = "Restaurant images/la_eskina_image.png")
                images["bocca_image"] = tk.PhotoImage(file = "Restaurant images/bocca_image.png")
                images["freddys_image"] = tk.PhotoImage(file = "Restaurant images/freddys_image.png")
                images["mass_avenue_image"] = tk.PhotoImage(file = "Restaurant images/mass_avenue_image.png")
                images["tin_roof_image"] = tk.PhotoImage(file = "Restaurant images/tin_roof_image.png")
                images["goodfellas_image"] = tk.PhotoImage(file = "Restaurant images/goodfellas_image.png")
                images["aw_image"] = tk.PhotoImage(file = "Restaurant images/aw_image.png")
                images["culvers_image"] = tk.PhotoImage(file = "Restaurant images/culvers_image.png")
                images["punch_bowl_image"] = tk.PhotoImage(file = "Restaurant images/punch_bowl_image.png")
                images["inferno_image"] = tk.PhotoImage(file = "Restaurant images/inferno_image.png")
                images["shapiros_image"] = tk.PhotoImage(file = "Restaurant images/shapiros_image.png")
                images["taxman_image"] = tk.PhotoImage(file = "Restaurant images/taxman_image.png")
                images["district_tap_image"] = tk.PhotoImage(file = "Restaurant images/district_tap_image.png")
                images["futuro_image"] = tk.PhotoImage(file = "Restaurant images/futuro_image.png")
                images["connors_image"] = tk.PhotoImage(file = "Restaurant images/connors_image.png")
                images["festiva_image"] = tk.PhotoImage(file = "Restaurant images/festiva_image.png")
                images["tenth_street_image"] = tk.PhotoImage(file = "Restaurant images/tenth_street_image.png")
                images["fresco_image"] = tk.PhotoImage(file = "Restaurant images/fresco_image.png")
                images["vida_image"] = tk.PhotoImage(file = "Restaurant images/vida_image.png")
                images["fountain_room_image"] = tk.PhotoImage(file = "Restaurant images/fountain_room_image.png")
                images["harry_and_izzys_image"] = tk.PhotoImage(file = "Restaurant images/harry_and_izzys_image.png")
                images["bluebeard_image"] = tk.PhotoImage(file = "Restaurant images/bluebeard_image.png")
                images["prime_image"] = tk.PhotoImage(file = "Restaurant images/prime_image.png")
                images["st_elmo_image"] = tk.PhotoImage(file = "Restaurant images/st_elmo_image.png")
                images["beholder_image"] = tk.PhotoImage(file = "Restaurant images/beholder_image.png")
                images["ocean_prime_image"] = tk.PhotoImage(file = "Restaurant images/ocean_prime_image.png")
                images["union_fifty_image"] = tk.PhotoImage(file = "Restaurant images/union_fifty_image.png")
                images["mesh_image"] = tk.PhotoImage(file = "Restaurant images/mesh_image.png")
        #Print missing images for error handling
        except tk.TclError as error:
            print(f"Error loading images {error}")
        return images

    #Initialize dictionaries for price tiers
    def initialize_dict(self, images):
        """Initialize dictionaries key being the restaurant name and get image being the value"""
        low_price = {
            "The Great Divide": images.get("great_divide_image"),
            "John’s Famous Stew": images.get("john_stew_image"),
            "La Eskina Indy": images.get("la_eskina_image"),
            "Bocca": images.get("bocca_image"),
            "Freddy’s": images.get("freddys_image"),
            "Mass Avenue Pub": images.get("mass_avenue_image"),
            "Tin Roof": images.get("tin_roof_image"),
            "Goodfellas Pizzaria": images.get("goodfellas_image"),
            "A&W Restaurant": images.get("aw_image"),
            "Culver’s": images.get("culvers_image")
        }

        medium_price = {
            "Punch Bowl Social" : images.get("punch_bowl_image"),
            "The Inferno Room" : images.get("inferno_image"),
            "Shapiro's Delicatessen" : images.get("shapiros_image"),
            "TaxMan Cityway" : images.get("taxman_image"),
            "The District Tap" : images.get("district_tap_image"),
            "Futuro" : images.get("futuro_image"),
            "Connor's Kitchen + Bar" : images.get("connors_image"),
            "Festiva" : images.get("festiva_image"),
            "10th Street Diner" : images.get("tenth_street_image"),
            "Fresco Italian Café" : images.get("fresco_image")
        }

        high_price = {
            "Vida": images.get("vida_image"),
            "The Fountain Room": images.get("fountain_room_image"),
            "Harry & Izzy's": images.get("harry_and_izzys_image"),
            "BlueBeard": images.get("bluebeard_image"),
            "Prime 47": images.get("prime_image"),
            "St. Elmo Steak House": images.get("st_elmo_image"),
            "Beholder": images.get("beholder_image"),
            "Ocean Prime": images.get("ocean_prime_image"),
            "Union 50": images.get("union_fifty_image"),
            "Mesh": images.get("mesh_image")
        }
        return low_price, medium_price, high_price

    def destroy_widgets(self):
        """Function to destroy all widgets"""
        for widget in self.root.winfo_children(): #For widget in root
            if widget != self.background_label: #Exclude background
                widget.destroy() #Destroy widget

    def welcome_screen(self):
        """Display welcome screen"""
        #Making widgets
        welcome_title = tk.Label(self.root, text = 'Having trouble deciding on a restaurant?', font = "Arial 20 bold")
        #Start button that initiates on_start function
        start_button = tk.Button(self.root, text = "Start!", font = "Arial 20 bold", bg = "dodger blue", fg = "white", command = self.on_start)

        #Configure grid
        self.root.columnconfigure((1, 2, 3, 4, 5), weight = 1)
        self.root.rowconfigure((1, 2, 3, 4, 5), weight = 1)

        #Arranging widgets
        welcome_title.grid(row = 2, column = 3, sticky = "s")
        start_button.grid(row = 3, column = 3, ipadx = 30, ipady = 10)


    def on_start(self):
        """Runs once start is clicked. This screen displays price tiers."""
        #Delete widgets
        self.destroy_widgets()

        #Create instance of ChooseRestaurant class with initialized price tier dictionaries
        rest_picker = ChooseRestaurant(self.low_price, self.medium_price, self.high_price)

        #Add widgets
        start_title = tk.Label(self.root, text = 'Choose a price tier', font = "Arial 25 bold")
        low_price_button = tk.Button(
            self.root,
            font = "Arial 16 bold",
            text = "$5 - $15",
            bg = "dodger blue", fg = "white",
            width = 10, height = 2,
            command = lambda: self.handle_restaurant_and_image(rest_picker.low_price_chosen(),"low")
        )

        medium_price_button = tk.Button(
            self.root,
            font = "Arial 16 bold",
            text = "$15 - $25",
            bg = "dodger blue", fg = "white",
            width = 10, height = 2,
            command = lambda: self.handle_restaurant_and_image(rest_picker.medium_price_chosen(),"medium")
        )
        high_price_button = tk.Button(
            self.root,
            font = "Arial 16 bold",
            text = "$50 - $100",
            bg = "dodger blue", fg = "white",
            width = 10, height = 2,
            command = lambda: self.handle_restaurant_and_image(rest_picker.high_price_chosen(),"high")
        )

        #Arrange widgets
        start_title.grid(row = 1, column = 3)
        low_price_button.grid(row = 2, column = 3)
        medium_price_button.grid(row = 3, column = 3)
        high_price_button.grid(row = 4, column = 3)

    def get_random_restaurant(self, tier_dict, exclude=None):
        """Get a random restaurant from the given dictionary, excluding a specific value."""
        restaurant = rd.choice(list(tier_dict.keys())) #Get random restaurant from tier dictionary
        while restaurant == exclude: #Prevents from picking same restaurant twice in a row
            restaurant = rd.choice(list(tier_dict.keys())) #Get new choice
        return restaurant, tier_dict.get(restaurant)

    def handle_restaurant_and_image(self, chosen_restaurant, price_tier):
        """Gets image and restaurant name """
        # Clear widgets
        self.destroy_widgets()
        #Map price tiers to corresponding dictionaries
        tier_mapping = {
            "low": self.low_price,
            "medium": self.medium_price,
            "high": self.high_price,
        }
        #Retrieve dictionary corresponding to price tier
        tier_dict = tier_mapping.get(price_tier)

        #Store price range for later use
        self.current_price_tier = price_tier

        #Stores the last restaurant(from try_another function) in a variable
        self.last_restaurant = chosen_restaurant

        #Get restaurant image
        image = tier_dict.get(chosen_restaurant)

        #Add restaurant label
        self.restaurant_label = tk.Label(self.root, text = f"Chosen Restaurant:\n{chosen_restaurant}", font = "Arial 20 bold")
        #Arrange restaurant label
        self.restaurant_label.grid(row = 1, column = 3, sticky = "s")

        #If an image is retrieved
        if image:
            #Add widgets
            self.restaurant_image = tk.Label(self.root, image = image, bg = "white")
            #Arrange widgets
            self.restaurant_image.grid(row = 3, column = 3)

        #If no image
        else:
            self.restaurant_image = tk.Label(self.root, text = "No image available", font = "Arial 20 italic", bg = "white")
            self.restaurant_image.grid(row = 3, column = 3)

        #Add widgets
        back_button = tk.Button(self.root, font = "Arial 15 bold", text = "Back", command = self.on_start)
        try_another_button = tk.Button(self.root, font = "Arial 15 bold", text = "Try Another", bg = "dodger blue", fg = "white", command = lambda: self.try_another())
        done_button = tk.Button(self.root, font = "Arial 15 bold", text = "End", bg = "white", command = lambda: self.end_program(self.last_restaurant))

        #Arrange widgets
        back_button.grid(row = 5, column = 1, padx = 20, sticky = 'w')
        try_another_button.grid(row = 5, column = 3,)
        done_button.grid(row = 5, column = 5, padx = 20, sticky = "e")

    def try_another(self):
        """Called when "try another" button is clicked.
        Handles getting another choice and updating widgets"""
        # Map price tiers to corresponding dictionaries
        tier_mapping = {
            "low": self.low_price,
            "medium": self.medium_price,
            "high": self.high_price,
        }

        #Get current price tier dictionary and assign to variable
        tier_dict = tier_mapping.get(self.current_price_tier)

        #Get a new restaurant and image with tier_dict, excluding the last restaurant.
        chosen_restaurant, image = self.get_random_restaurant(tier_dict, exclude=self.last_restaurant)

        #Update last_restaurant
        self.last_restaurant = chosen_restaurant

        #Update restaurant label
        self.restaurant_label.config(text = f"Chosen Restaurant:\n{chosen_restaurant}")

        #If an image is retrieved
        if image:
            #Update image
            self.restaurant_image.config(image = image)
            self.restaurant_image.grid(row = 3, column = 3)

        #If no image is retrieved
        else:
            #Don't show image and display text
            self.restaurant_image.config(image = '', text = "No image available" , font = "Arial 20 bold")

    def end_program(self, last_restaurant):
        """Open second window that displays final restaurant and thank you message"""
        #Hide our Main window(don't delete because we need to use last_restaurant)
        self.root.withdraw()

        #Initialize second window
        second_window = tk.Toplevel(self.root)
        second_window.title("Thank you!")
        second_window.geometry("300x300+500+500")
        second_window.resizable(False, False)

        #Configure rows and columns for second window
        second_window.columnconfigure((1, 2, 3, 4, 5), weight=1)
        second_window.rowconfigure((1, 2, 3, 4, 5), weight=1)

        #Add widgets
        thank_you_label = tk.Label(second_window, text = 'Thank you for using my program!', font = "Arial 10 bold")
        enjoy_label = tk.Label(second_window, text = f"Enjoy your food at {last_restaurant}!", font = "Arial 10 bold")
        exit_button = tk.Button(second_window, text = "Exit", font = ("Arial", 10, "bold"), bg = "red", fg = "white", command = self.root.destroy)

        #Arrange widgets
        thank_you_label.grid(row = 2, column = 3)
        enjoy_label.grid(row = 3, column = 3)
        exit_button.grid(row = 4, column = 3)

def main():
    """Main function"""
    # Initialize root
    root = tk.Tk()

    # Set the title
    root.title('Indianapolis restaurant chooser')

    # Set dimensions
    root.geometry('600x600+300+300')
    root.resizable(False, False)
    background_image = tk.PhotoImage(file = "Restaurant Images/background_image.png")
    background_label = tk.Label(root, image = background_image)
    background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    root.background_image = background_image

    #Initialize instance of Application class
    app = Application(root)

    #Executes our program and waits for clicks
    root.mainloop()

if __name__ == "__main__":
    main()