import requests
 
response = requests.get('https://www.hdwallpapers.in/download/colorful_glowing_shape_lines_4k_8k_hd_abstract-HD.jpg')
with open('img.jpg', 'wb') as picture:
    picture.write(response.content)