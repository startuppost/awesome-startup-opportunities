import json

# Load the JSON data
with open('opportunities.json', 'r') as file:
  data = json.load(file)

# Initialize markdown content
md_content = "# Opportunities\n\n"

# Generate markdown for each opportunity
for opp in data['opportunities']:
  md_content += f"## [{opp['title']}]({opp['url']})\n"
  md_content += f"- Organizer: {opp['organizer']}\n"
  md_content += f"- Types: {', '.join(opp['types'])}\n"
  md_content += f"- Topics: {', '.join(opp['topics'])}\n"
  md_content += f"- Location: {opp['location']}\n"
  md_content += f"- Eligibility: {', '.join(opp['eligibility'])}\n"
  md_content += f"- Description: {opp['description']}\n"
  md_content += f"- Expire Date: {opp['expireDate']}\n"
  md_content += f"- Hook Status: {opp['hookStatus']}\n"
  md_content += f"- Prize Value: {opp['prizeValue']}\n"
  md_content += f"- Pinned: {opp['pinned']}\n"
  md_content += f"- User: {opp['user']}\n\n"

# Write the markdown content to a README.md file
with open('README.md', 'w') as file:
  file.write(md_content)