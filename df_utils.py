import os
import pandas as pd
from urllib.parse import unquote
import wikipedia

# Gallery of sovereign state flags. Make initial Dataframe.
def create_dataframe(path, csv_file_name):
  '''
  This function takes in a path and a complete csv file name
  Ex. path = './', csv_file_name = 'my_csv_file.csv'.
  It returns a dataframe and saves a csv of that same name in that path.
  '''
  flags = pd.DataFrame(columns=['country_name', 'wiki_img_url', 'flag_file_name'])

  page = wikipedia.page("Gallery of sovereign state flags")
  all_images = page.images

  # Reset dataframe in case of existing data
  flags.reset_index(drop=True, inplace=True)
  i = 0
  for image in all_images:
    if 'Flag' in image or 'Bandera' in image:
      flags.loc[i, 'wiki_img_url'] = image
      i += 1

  def get_country_names(x):
    res = x.split('/')[-1].split('.svg')[0].split('_')[2:]
    res = ' '.join(res).title()
    if '28' in res:
      res = res.split(' %')[0]
    res = unquote(res)
    return res

  # Populate dataframe.
  flags['country_name'] = flags['wiki_img_url'].apply(get_country_names)
  flags['flag_file_name'] = flags['country_name'].apply(lambda x: '_'.join(x.split()))
  flags.to_csv(path + csv_file_name, index=False)

  return flags

# This is the main function which generates the primary data.
def gen_data(path, csv_file_name):
  '''
  Usage: my_df = gen_data('./', 'my_file.csv')
  This function returns a dataframe.
  '''
  csv_found = False
  # Checks if a file exists in a certain directory.
  file_path = os.path.join(path, csv_file_name)
  # Use the os.path.exists() function to check if the file exists.
  csv_found = os.path.exists(file_path)

  if csv_found:
    print('The file exists. Reading from csv.')
    flags = pd.read_csv(file_path)
  else:
    print('The file does not exist. Creating new Dataframe.')
    flags = create_dataframe(path, csv_file_name)

  return flags

# my_df = gen_data('./', 'my_file.csv')
# print(my_df.head())
