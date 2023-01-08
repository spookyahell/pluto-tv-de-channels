import json

with open('pluto-tv-de_channels.json') as f:
	file_contents = f.read()
	
README = '''# pluto-tv-de-channels
**Description:** Pluto TV (DE) Channel information

**Disclaimer:** All information is publicly accessible for anyone with Germany IP address

The following file contains the raw data: [pluto-tv-de_channels.json](pluto-tv-de_channels.json)

Where inserted, the item `featuredOrder` has been removed from the individual channels as it seems to be a ever changing value.

## Access the channels m3u8 streams
It's possible to access the channels m3u8 by inserting the id # of the channel.

The way it works is:<br>
`https://service-stitcher-ipv4.clusters.pluto.tv/v2/stitch/hls/channel/{channel_id}/master.m3u8`<br>
(Replace `{channel_id}` with the respective value of the  id # field of the channel.)

## Changes to PlutoTV channels*
*_since the existance of this project_
### January 2023
* 2023-01-06: [new channel] "Pluto TV liebt Elvis" has been added (pop-up channel: _declared to be short-lived in summary_)

## Channels on PlutoTV in Germany

'''

table_heading = '''<table>
	<tr>
		<th>Channel logo</th>
		<th>Channel name</th>
		<th>Channel slug</th>
		<th>Channel hash</th>
		<th>id #</th>
		<th>Summary</th>
		<th>All image links</th>
	</tr>'''	


html_source = '''<html>
<head>
	<title>Pluto-TV (DE) Channels</title>
	<style>body {background-color: black; color:white}
table {background-color: gray}
table td,th {background-color: black}
table a:link {color:green}
table a:visited {color:orange}
table a:hover {color:grey}
table a:active {color:yellow}
	</style>
</head>
<body>
<h1>Channels on PlutoTV in Germany</h1>

'''

html_source += table_heading
README += table_heading

jso = json.loads(file_contents)

for channel in jso['data']:
	channel_name = channel['name']
	channel_slug = channel['slug']
	channel_hash = channel['hash']
	channel_id = channel['id']
	channel_summary = channel['summary']
	m3u8_path = channel['stitched']['paths'][0]['path']
	channel_images = channel['images']
	
	channel_image_links_html = ''
	for image in channel_images:
		image_url = image['url']
		image_type = image['type']
		if image['type'] == 'colorLogoPNG':
			color_logo_src = image_url
		if channel_images.index(image) == len(channel_images)-1:
			new_line = ''
		else:
			new_line = '''<br>
			'''
		channel_image_links_html += f'<a href="{image_url}" target="_blank">{image_type}</a>{new_line}'

	add_column = f'''
	<tr>
		<td><img src="{color_logo_src}" width="200px"></td>
		<td>{channel_name}</td>
		<td>{channel_slug}</td>
		<td>{channel_hash}</td>
		<td>{channel_id}</td>
		<td>{channel_summary}</td>
		<td>
			{channel_image_links_html}
	</tr>'''
	
	README += add_column
	html_source += add_column

README + '\n</table>'
html_source + '\n</table>\n</body>'

with open('README.md', 'w', encoding = 'utf-8-sig') as f:
	f.write(README)
	
with open('index.html', 'w', encoding = 'utf-8-sig') as f:
	f.write(html_source)