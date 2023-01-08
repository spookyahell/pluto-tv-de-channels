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
`https://service-stitcher-ipv4.clusters.pluto.tv/v2/stitch/hls/channel/{channel_id}/master.m3u8`

## Changes to PlutoTV channels*
*_since the existance of this project_
### January 2023
* 2023-01-06: [new channel] "Pluto TV liebt Elvis" has been added (pop-up channel: _declared to be short-lived in summary_)

## Channels on PlutoTV in Germany

<table>
	<tr>
		<th>Channel logo</th>
		<th>Channel name</th>
		<th>Channel slug</th>
		<th>Channel hash</th>
		<th>id #</th>
		<th>Summary</th>
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
		<td>
			{channel_image_links_html}
	</tr>'''

README + '\n</table>'

with open('README.md', 'w', encoding = 'utf-8-sig') as f:
	f.write(README)