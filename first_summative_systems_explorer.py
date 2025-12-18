import sys
import time
aspect_choice = ""
stakeholder_production = ""
learn_more = ""
# This is the set-up for the code, importing functions that are needed, and assigning values to variable that are needed later

def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0125)
# This is the typewrter sort of effect function, that makes the outputted text typed out


typing_effect("Welcome to the Systems Explorer! In this program, you will be able to explore and learn about the different stakeholders in a system.")
print("")
typing_effect("The system that you, the user, will be exploring is analog watches. Watches are a common accessory that many people use to keep track of time and make a fashion statement.")
print("")
typing_effect("Analog watches, specifically, are watches that use a traditional clock face with hour and minute hands to display the time, as opposed to digital watches that use a numerical display.")
print("")
typing_effect("Press ENTER to continue...")
input("")
# This is the introduction, where the purpose of the code is explained and it goes over what will be talked about


typing_effect("There are a few categories that stakeholders fall under, those being production, consumption and disposal. Each category has its own unique stakeholders that play a role in the watch industry.")
print("")
while aspect_choice not in ["production", "consumption", "disposal"]:
    typing_effect("Which category of the watch industry would you like to explore? (production, consumption, disposal): ")
    aspect_choice = input("").lower()
    if aspect_choice not in ["production", "consumption", "disposal"]:
        print("Invalid choice. Please choose either 'production', 'consumption', or 'disposal'.")
# First input as to what apsect of the stakeholders the user wants to explore


if aspect_choice == "production": # If production is picked as the aspect to be explored, all of this information will unfold
    print("")
    typing_effect("The production of watches is essentially all that is required for the watch to be made. This includes the sourcing and assembly of the watch.")
    print("")
    typing_effect("The sourcing of the watch includes where the different materials for the watch are obtained. This includes the metal for the case, the crystal for the face, and the leather or metal for the band.")
    print("")
    typing_effect("The assembly of the watch includes the process of putting all the different parts together to create the final product. This can be done by hand or by machine, depending on the type and quality of watch being produced.")
    print("")
    while stakeholder_production not in ["watchmakers", "leather", "ore"]:
        typing_effect("Which stakeholder in the production of watches would you like to learn more about? (watchmakers, leather, ore): ")
        stakeholder_production = input("").lower()
        if stakeholder_production not in ["watchmakers", "leather", "ore"]:
            print("Invalid choice. Please choose either 'watchmakers', 'leather', or 'ore'.")
    if stakeholder_production == "watchmakers":
        time.sleep(0.5)
        print("")
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        time.sleep(0.5)
        typing_effect("What are some countries that have a reputation of watchmaking? (Type your answer): ")
        countries = input("").lower()
        if countries in ["switzerland", "japan", "germany", "france", "italy", "united kingdom", "uk"]:
            typing_effect("Great job! That's a great answer. Here is a full list of countries known for their watchmakers: Switzerland, Japan, Germany, France, Italy, and the United Kingdom.")
        else:
            typing_effect("Thats a great answer! Some more examples of countries with a reputation for watchmaking include Switzerland, Japan, Germany, France, Italy, and the United Kingdom.")
        time.sleep(0.5)
        print("")
        typing_effect("Watchmakers are the people and companies that design, assemble, and sell watches. They are responsible for creating the final product that consumers purchase.")
        print("")
        typing_effect("Watchmakers can range from small, independent companies to large, multinational corporations. Some well-known watchmakers include Rolex, Omega, Seiko, and Citizen.")
        print("")
        typing_effect("Watchmakers also often influence the fashion and style of watches, as they are the ones who design and create the different styles and trends.")
        print("")
        typing_effect("Countries also gain a lot of fame for being known for their watchmakers. Switzerland is perhaps the most famous country for watchmaking, with many high-end and luxury watch brands originating from there.")
        print("")
        typing_effect("Certain watches however are not created by watchmakers, and actually are created in factories. These watches are usually more affordable, but lack the craftsmanship and quality of watches made by watchmakers.")
        print("")
        typing_effect("If you want to get a high quality watches, it is best to go with a reputable watchmaker, as they will have the experience and expertise to create a well-made product.")
    if stakeholder_production == "leather":
        time.sleep(0.5)
        print("")
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        time.sleep(0.5)
        typing_effect("What one animal that leather comes from? (Type your answer): ")
        leather = input("").lower()
        if leather in ["goat", "sheep", "cow", "pig", "alligator", "ostritch", "stingray", "snake"]:
            typing_effect("Great job! That's a great answer. Here is a full list of common leather sourcing animals: cow, pig, sheep, goat, stingray, ostritch, snake and alligator.")
        else:
            typing_effect("Thats a great answer! Some more examples of common leather sourcing animals include cow, pig, sheep, goat, stingray, ostritch, snake and alligator.")
        time.sleep(0.5)
        print("")
        typing_effect("Leather is a material made from drying and processing animal skins. Leather is commonly used in watch bands, as it is durable and comfortable to wear.")
        print("")
        typing_effect("Because leather is made from animal skins, there are some problems with its sourcing. The main issues with leather is the treatment of the animals, and the poaching of endangered and exotic species for their skins.")
        print("")
        typing_effect("Many common animals used for leather are kept in poor conditions, and are often subjected to inhumane treatment. This includes cramped living spaces, lack of proper food and water, and even abuse.")
        print("")
        typing_effect("Exotic and endangered species, like alligator, ostritch, and stingray are often poached for their skins, which are then sold on the black market. This is a huge issue, as it contributes to the decline of these species in the wild.")
        print("")
        typing_effect("It is important to be aware of these issues when purchasing a watch with a leather band, and to try and support companies that source their leather ethically. A way to be sure of this is to look for certifications like the Leather Working Group (LWG).")
    if stakeholder_production == "ore":
        time.sleep(0.5)
        print("")
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        time.sleep(0.5)
        typing_effect("What are some common ores and jewels used in watches? (Type your answer): ")
        ore = input("").lower()
        if ore in ["gold", "silver", "steel", "titanium", "sapphire", "diamond", "platinum", "brass"]:
            typing_effect("Great job! That's a great answer. Here is a full list of common ores and jewels used in watches: gold, silver, steel, titanium, sapphire, diamond, platinum, and brass.")
        else:    
            typing_effect("Those are some good answers! Some more examples of common ores and jewels used in watches include gold, silver, steel, titanium, sapphire, diamond, platinum, and brass.")
        time.sleep(0.5)
        print("")
        typing_effect("Ores and jewels are a very important part of wristwatches, as they are used for most parts of watches.")
        print("")
        typing_effect("These metals and crystals are often very valuable and expensive, making them very sought after. As with any valuable material, this usually results in issues with the sourcing.")
        print("")
        typing_effect("Oftentimes, unfair treatment is involved when it comes to mining these ores. This includes child labour, low pay, even abuse and harm. These workers are known as blood diamond workers (even if the ore being mined is not diamonds).")
        print("")
        typing_effect("Blood mines are extremely unethical and inhumane, and are a huge issue in the mining industry. Many companies are now trying to source their materials from ethical and fair sources, but it is still a prevalent issue.")
        print("")
        typing_effect("Blood mining usually takes place in developing countries, like the DRC and Angola, where there are less regulations and oversight. This makes it easier for companies to exploit workers and get away with unethical practices.")
        print("")
        typing_effect("It is important to be aware of these issues when purchasing a watch, and to try and support companies that source their materials ethically. A way to be sure of this is to look for certifications like Fair Trade.")


if aspect_choice == "consumption": # If consumption is picked as the aspect to be explored, all of this information will unfold
    print("")
    typing_effect("After the production of watches, they are then sold to consumers. Consumers are the entities who purchase and use the watches. This includes individuals, retailers, and even companies that buy watches in bulk for their employees.")
    print("")
    typing_effect("Consumers play a crucial role in the watch industry, as they are the ones who drive demand for watches. The preferences and purchasing habits of consumers can greatly influence the types of watches that are produced and sold.")
    while stakeholder_production not in ["individuals", "industries", "retailers"]:
        typing_effect("Which stakeholder in the production of watches would you like to learn more about? (individuals, industries, watch retailers): ")
        stakeholder_production = input("").lower()
        if stakeholder_production not in ["individuals", "industries", "watch retailers"]:
            print("Invalid choice. Please choose either 'individuals', 'industries', or 'retailers'.")
    if stakeholder_production == "individuals":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        typing_effect("What are some watches that have high demand, and are often purchased by individuals? (Type your answer): ")
        individuals = input("").lower()
        if individuals in ["rolex", "omega", "cartier", "audemars piguet", "breitling", "tudor", "hublot", "panerai"]:
            typing_effect("Great job! That's a great answer. Here is a full list of common watch brands: rolex, omega, cartier, audemars piguet, breitling, tudor, hublot, and panerai.")
        else:    
            typing_effect("Those are some good answers! Some more examples of common watch brands include rolex, omega, cartier, audemars piguet, breitling, tudor, hublot, and panerai.")
        time.sleep(0.5)
        print("")
        typing_effect("Individuals are the most common type of consumer in the watch industry. They purchase watches for personal use, either for practical purposes (to tell time) or for fashion and style.")
        print("")
        typing_effect("Individuals can have a wide range of preferences when it comes to watches, from high-end luxury brands to more affordable and practical options. Their purchasing habits can greatly influence the types of watches that are produced and sold.")
        print("")
        typing_effect("Many individuals also collect watches as a hobby, which can drive demand for rare and unique timepieces.")
    if stakeholder_production == "industries":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        typing_effect("What are some of the industries that purchase watches for their employees, and have specific requirements with these watches, in order to fit their purpose? (Type your answer): ")
        individuals = input("").lower()
        if individuals in ["military", "army", "law enforcement", "hospitality", "modelling"]:
            typing_effect("Great job! That's a great answer. The industries that most commonly purchase watches for their employees include the military, law enforcement, modelling and hospitality.")
        else:    
            typing_effect("Thats an interesting answer! Some examples of industries that commonly purchase watches include the military, law enforcement, modelling and hospitality.")
        time.sleep(0.5)
        print("")
        typing_effect("Industries are another important type of consumer in the watch industry. Many companies purchase watches in bulk for their employees, either as part of a uniform or as a promotional item.")
        print("")
        typing_effect("Industries can also influence the types of watches that are produced and sold, as they may have specific requirements or preferences for the watches they purchase.")
        print("")
        typing_effect("For example, some industries, such as militaries, may require watches with specific features, such as water resistance or durability, which can drive demand for certain types of watches.")
        print("")
        typing_effect("Some common industries that purchase watches for their employees include the military, law enforcement, and hospitality. These industries often require watches that are durable, reliable, and functional.")
    if stakeholder_production == "retailers":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        print("")
        typing_effect("Retailers are another important type of consumer in the watch industry. They purchase watches from watchmakers and sell them to individuals and other consumers.")
        print("")
        typing_effect("Retailers can greatly influence the types of watches that are produced and sold, as they often have a say in what products are stocked and promoted in their stores.")
        print("")
        typing_effect("Some well-known watch retailers include department stores, jewelry stores, and specialty watch shops. These retailers often carry a wide range of watch brands and styles to cater to different consumer preferences.")
        print("")
        typing_effect("Retailers also play a crucial role in marketing and promoting watches to consumers, which can drive demand for certain types of watches.")


if aspect_choice == "disposal": # If disposal is picked as the aspect to be explored, all of this information will unfold
    print("")
    typing_effect("After the consumption of watches, they must then be disposed of. The stakeholders involved in disposal are responsible for what happens after the system is discarded.")
    print("")
    typing_effect("The disposal of watches can involve recycling, refurbishing, or other methods to manage waste and reduce environmental impact.")
    print("")
    typing_effect("Another method of disposal is donation, where watches that are still functional are given to those in need or to organizations that can repurpose them.")
    print("")
    typing_effect("While recycling and donating are common methods of disposal, there are still many watches that end up in landfills, contributing to environmental pollution.")
    print("")
    while stakeholder_production not in ["recycling", "landfills", "donation"]:
        typing_effect("Which stakeholder in the disposal of watches would you like to learn more about? (recycling, landfills, donation): ")
        stakeholder_production = input("").lower()
        if stakeholder_production not in ["recycling", "landfills", "donation"]:
            print("Invalid choice. Please choose either 'recycling', 'landfills', or 'donation'.")
    if stakeholder_production == "recycling":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        typing_effect("What are materials that are often recycled on a daily basis? (Type your answer): ")
        recycling = input("").lower()
        if recycling in ["paper", "plastic", "metal", "glass"]:
            typing_effect("Great job! That's a great answer. The materials that are often recycled on a daily basis include paper, plastic, metal, and glass.")
        else:    
            typing_effect("Thats an interesting answer! Some examples of materials that commonly get recycled include paper, plastic, metal, and glass.")
        time.sleep(0.5)
        print("")
        typing_effect("Recycling is a crucial stakeholder in the disposal of watches. It involves breaking down the watch into its component materials and reprocessing them for use in new products.")
        print("")
        typing_effect("Recycling helps to reduce waste and conserve natural resources, as it allows for the reuse of valuable materials like metals and plastics.")
        print("")
        typing_effect("Many watchmakers and companies now offer recycling programs for their products, allowing consumers to return their old watches for proper recycling.")
        print("")
        typing_effect("It is important to properly recycle watches, as they can contain hazardous materials like batteries and certain metals that can harm the environment if not disposed of correctly.")
    if stakeholder_production == "landfills":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        typing_effect("What are materials that end up in landfills? (Type your answer): ")
        landfills = input("").lower()
        if landfills in ["plastic", "ceramics", "glass", "food waste"]:
            typing_effect("Great job! That's a great answer. The materials that end up in landfills include ceramics, plastic, food waste, and glass.")
        else:    
            typing_effect("Thats an interesting answer! Some examples of materials that get sent to landfills include ceramics, plastic, food waste, and glass.")
        time.sleep(0.5)
        print("")
        typing_effect("Landfills are unfortunately a common method of disposal for watches. When watches are thrown away in the trash, they often end up in landfills, where they can take years to decompose.")
        print("")
        typing_effect("Watches can contain hazardous materials like batteries and certain metals that can leach into the soil and water, causing environmental pollution.")
        print("")
        typing_effect("It is important to try and avoid sending watches to landfills by recycling or donating them instead. This helps to reduce waste and minimize the environmental impact of watch disposal.")
    if stakeholder_production == "donation":
        typing_effect("Let's do a quick quiz before we continue, just to test your knowledge!")
        print("")
        time.sleep(0.5)
        typing_effect("What are some organizations (types or specific examples) that accept donations? (Type your answer): ")
        donation = input("").lower()
        if donation in ["salvation army", "goodwill", "food banks", "charity shops"]:
            typing_effect("Great job! That's a great answer. Some common organizations that accept donations include Salvation Army, Goodwill, Food Banks, and Charity Shops.")
        else:    
            typing_effect("Thats an interesting answer! Some examples of organizations that accept donations include Salvation Army, Goodwill, Food Banks, and Charity Shops.")
        time.sleep(0.5)
        print("")
        typing_effect("Donation is a great way to dispose of watches that are still functional. Many organizations accept donations of watches to give to those in need or to repurpose them.")
        print("")
        typing_effect("Donating watches helps to extend their lifespan and reduce waste, as it allows them to be used by someone else instead of being thrown away.")
        print("")
        typing_effect("There are many organizations that accept watch donations, including charities, thrift stores, and watch repair shops. It is important to ensure that the watches being donated are in good condition and still functional.")
# In all of the previous code, quizzes were included to be more interactive and get user input, and depending on the stakeholder and aspect chosen, the code would continue differently

print("")
typing_effect("Now that you have explored the different stakeholders in the watch industry, you have a better understanding of the complex system that goes into creating, using, and disposing of watches.")
print("")
typing_effect("If you would like to choose another aspect to explore, please close and reopen the program.")
print("")
typing_effect("If you would like to learn more about the actual system of watches, type 'learn more' when prompted below.")
print("")
typing_effect("If you would like to find other sources to learn more about watches, type 'other sources' when prompted below.")
print("")
typing_effect("If you would like to exit the program, type 'exit' when prompted below, or close the program")
print("")
# Allows users the choice of ending the program, learning about watches (not the stakeholders), or finding more sources so they can conduct their own research.
while learn_more not in ["learn more", "other sources", "exit"]:    
    typing_effect("Would you like to learn more about the actual system of watches? (learn more/other sources/exit): ")
    learn_more = input("").lower()
    if learn_more not in ["learn more", "other sources", "exit"]:
        print("Invalid choice. Please choose either 'learn more', 'other sources', or 'exit'.")
if learn_more == "learn more":
    print("")
    typing_effect("Watches are intricate devices that combine both art and science to keep accurate time. The core mechanism of a watch is known as the movement, which can be either mechanical or quartz.")
    print("")
    typing_effect("Mechanical watches use a complex system of gears and springs to measure time, while quartz watches use an electronic oscillator regulated by a quartz crystal.")
    print("")
    typing_effect("In addition to the movement, watches also consist of various components such as the case, dial, hands, and strap or bracelet. Each component plays a crucial role in the overall functionality and aesthetics of the watch.")
    print("")
    typing_effect("Watches can also come with various features and complications, such as chronographs, date displays, and water resistance, which add to their functionality and appeal.")
    print("")
    typing_effect("Overall, watches are a fascinating blend of craftsmanship, technology, and design that have captivated people for centuries.")
    print("")
    typing_effect("Thank you for using the Systems Explorer! We hope you enjoyed learning about the stakeholders in the watch industry and the fascinating world of watches.")
elif learn_more == "other sources":
    print("")
    typing_effect("Here are some sources where you can learn more about watches:")
    print("")
    typing_effect("1. 'The Wristwatch Handbook' by Ryan Schmidt - This book provides a comprehensive explanation of how watches work and features of different watches.")
    print("")
    typing_effect("2. 'The Great Watch Book' by Dominik Hofrichter - An in depth exploration of the history, design, and technology of watches.")
    print("")
    typing_effect("3. 'A Man's Guide to Wristwatches' (website - https://www.artofmanliness.com/style/accessories/mans-guide-wristwatches-choose-watch/) - This website offers articles, reviews, and guides on various aspects of watches.")
    print("")
    typing_effect("Thank you for using the Systems Explorer! We hope you enjoyed learning about the stakeholders in the watch industry and found these resources helpful.")
elif learn_more == "exit":
    typing_effect("Thank you for using the Systems Explorer! We hope you enjoyed learning about the stakeholders in the watch industry.")
