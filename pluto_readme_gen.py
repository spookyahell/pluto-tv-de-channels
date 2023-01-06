import json

with open('pluto-tv-de_channels.json') as f:
	file_contents = f.read()
	
README = '''# pluto-tv-de-channels
**Description:** Pluto TV (DE) Channel information

**Disclaimer:** All information is publicly accessible for anyone with Germany IP address

The following file contains the raw data: [pluto-tv-de_channels.json](pluto-tv-de_channels.json)

Where inserted, the item `featuredOrder` has been removed from the individual channels as it seems to be a ever changing value.

## Channels on PlutoTV in Germany

<table>
	<tr>
		<th>Channel logo</th>
		<th>Channel name</th>
		<th>Channel slug</th>
		<th>Channel hash</th>
		<th>id #</th>
		<th>Summary</th>
		<th>Path</th>
		<th>All image links</th>
	</tr>'''
	
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

	README += f'''
	<tr>
		<td><img src="{color_logo_src}"></td>
		<td>{channel_name}</td>
		<td>{channel_slug}</td>
		<td>{channel_hash}</td>
		<td>{channel_id}</td>
		<td>{channel_summary}</td>
		<td><code>{m3u8_path}</code></td>
		<td>
			{channel_image_links_html}
	</tr>'''

README + '\n</table>'

with open('README.test.md', 'w', encoding = 'utf-8-sig') as f:
	f.write(README)