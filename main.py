import requests
import os
import pandas as pd

def get_game_details(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()

    if data[str(app_id)]['success']:
        game_data = data[str(app_id)]['data']
        details = {}

        if 'type' in game_data:
            details['type'] = game_data['type']
        else:
            details['type'] = ''
        if 'name' in game_data:
            details['name'] = game_data['name']
        else:
            details['name'] = ''
        if 'steam_appid' in game_data:
            details['steam_appid'] = game_data['steam_appid']
        else:
            details['steam_appid'] = ''
        if 'required_age' in game_data:
            details['required_age'] = game_data['required_age']
        else:
            details['required_age'] = ''
        if 'controller_support' in game_data:
            details['controller_support'] = game_data['controller_support']
        else:
            details['controller_support'] = ''
        if 'dlc' in game_data:
            details['dlc'] = game_data['dlc']
        else:
            details['dlc'] = ''
        if 'detailed_description' in game_data:
            details['detailed_description'] = game_data['detailed_description']
        else:
            details['detailed_description'] = ''
        if 'about_the_game' in game_data:
            details['about_the_game'] = game_data['about_the_game']
        else:
            details['about_the_game'] = ''
        if 'short_description' in game_data:
            details['short_description'] = game_data['short_description']
        else:
            details['short_description'] = ''
        if 'fullgame' in game_data:
            details['fullgame'] = game_data['fullgame']
        else:
            details['fullgame'] = ''
        if 'supported_languages' in game_data:
            details['supported_languages'] = game_data['supported_languages']
        else:
            details['supported_languages'] = ''
        if 'header_image' in game_data:
            details['header_image'] = game_data['header_image']
        else:
            details['header_image'] = ''
        if 'website' in game_data:
            details['website'] = game_data['website']
        else:
            details['website'] = ''
        if 'pc_requirements' in game_data:
            details['pc_requirements'] = game_data['pc_requirements']
        else:
            details['pc_requirements'] = ''
        if 'mac_requirements' in game_data:
            details['mac_requirements'] = game_data['mac_requirements']
        else:
            details['mac_requirements'] = ''
        if 'linux_requirements' in game_data:
            details['linux_requirements'] = game_data['linux_requirements']
        else:
            details['linux_requirements'] = ''
        if 'legal_notice' in game_data:
            details['legal_notice'] = game_data['legal_notice']
        else:
            details['legal_notice'] = ''
        if 'drm_notice' in game_data:
            details['drm_notice'] = game_data['drm_notice']
        else:
            details['drm_notice'] = ''
        if 'ext_user_account_notice' in game_data:
            details['ext_user_account_notice'] = game_data['ext_user_account_notice']
        else:
            details['ext_user_account_notice'] = ''
        if 'developers' in game_data:
            details['developers'] = game_data['developers']
        else:
            details['developers'] = ''
        if 'publishers' in game_data:
            details['publishers'] = game_data['publishers']
        else:
            details['publishers'] = ''
        if 'demos' in game_data:
            details['demos'] = game_data['demos']
        else:
            details['demos'] = ''
        if 'price_overview' in game_data:
            details['price'] = game_data['price_overview']['final_formatted']
        else:
            details['price'] = '0' if game_data['is_free'] else 'price not available'

        return details
    else:
        return 'details not found'

# Read the existing CSV file
app_details = "app_details.csv"
index_file = "index.csv"
exists = os.path.isfile(app_details)

# Create an empty list to store game details
game_details_list = []
df = pd.read_csv("app_list.csv")
# Iterate over each row in the DataFrame
for i in range(len(df)):
    app_id = df["appid"][i]
    game_details = get_game_details(app_id)
    game_details_list.append(game_details)

# Convert the list of dictionaries into a DataFrame
game_details_df = pd.DataFrame(game_details_list)

# Add column names to the game details DataFrame
column_names = ['type', 'name', 'steam_appid', 'required_age', 'controller_support', 'dlc', 
                'detailed_description', 'about_the_game', 'short_description', 'fullgame', 
                'supported_languages', 'header_image', 'website', 'pc_requirements', 
                'mac_requirements', 'linux_requirements', 'legal_notice', 'drm_notice', 
                'ext_user_account_notice', 'developers', 'publishers', 'demos', 'price']
game_details_df.columns = column_names

# Write to the CSV file
if not exists:
    # Write both column names and details
    game_details_df.to_csv(app_details, mode='w', header=True, index=False)
else:
    # Append details only
    game_details_df.to_csv(app_details, mode='a', header=False, index=False)

# Save index to a separate file
if not exists:
    index_df = pd.DataFrame(df.index, columns=['index'])
    index_df.to_csv(index_file, index=False)
