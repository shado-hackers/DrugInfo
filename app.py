from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from pyrogram import *
from configs.telegram import api_id,api_hash,bot_token,bot_name
from core.drugload import load_products_from_csv
from configs.dataset import drug_data
from core.search_drug import search_product
from core.close_match import find_closest_match
import csv
import difflib

products = load_products_from_csv(drug_data)
app = Client(bot_name,api_id=api_id,api_hash=api_hash,bot_token=bot_token)

@app.on_message(filters.command('start'))
async def start_msg(client,message):
    name=str(message.from_user.first_name)
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        user_name = str(message.from_user.username)
        language_code = str(message.from_user.language_code)
        await message.reply(f"__Hey {name}__!\n\nI'm **DrugInfo bot** with an extensive database of medicines helps you to retrieve the vital informations of an medicine such as  product name, salt composition, price, manufacturer, description, side effects.\n\nJust let me know the medicine you want to search ?")
    except:
        pass

        
@app.on_message(filters.text)
async def drug(client,message):
    user_id = str(message.from_user.id)
    product_name = str(message.text)
    print(user_id)
    result = search_product(products, product_name)

    if result == "Product not found.":
        closest_match = find_closest_match(products, product_name)
        if closest_match:
            print(f"\nDid you mean: {closest_match}?")
            result = search_product(products, closest_match)
            if result != "Product not found.":
                product_info = dict(result.items())
                sub_catagory = product_info['sub_category']
                medicine_desc = product_info['medicine_desc']
                salt_composition = product_info['salt_composition']
                product_price = product_info['product_price']
                product_manufactured = product_info['product_manufactured']
                side_effects = product_info['side_effects']
                drug_interactions = product_info['drug_interactions']
                await message.reply(f"\n__Did you mean: {closest_match}?__\n\n**Category :**\n__{sub_catagory}__\n\n**Salt Composition :\n**__{salt_composition}__\n\n**Price : **__{product_price}__\n\n**Manufacture : **\n__{product_manufactured}__\n\n**Description : **\n\n__{medicine_desc}__\n\n**Side Effects :**\n\n__{side_effects}__\n\n")
                
        else:
            await message.reply("Drug not found.")
    else:
        print("\nProduct Information:")
        product_info = dict(result.items())
        sub_catagory = product_info['sub_category']
        medicine_desc = product_info['medicine_desc']
        salt_composition = product_info['salt_composition']
        product_price = product_info['product_price']
        product_manufactured = product_info['product_manufactured']
        side_effects = product_info['side_effects']
        drug_interactions = product_info['drug_interactions']
        await message.reply(f"\n__Did you mean: {product_info['product_name']}?__\n\n**Category :**\n__{sub_catagory}__\n\n**Salt Composition :\n**__{salt_composition}__\n\n**Price : **__{product_price}__\n\n**Manufacture : **\n__{product_manufactured}__\n\n**Description : **\n\n__{medicine_desc}__\n\n**Side Effects :**\n\n__{side_effects}__\n\n")
app.run()