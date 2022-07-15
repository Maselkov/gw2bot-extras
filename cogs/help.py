import discord
from discord import app_commands, ButtonStyle
from discord.ext import commands

EMOJIS = {
    "kofi": 997065288837234708,
    "github": 997065278464733224,
    "patreon": 997065282440925194,
    "paypal": 997065286463258654
}


class HelpView(discord.ui.View):

    def __init__(self, bot):
        super().__init__(timeout=None)
        emojis = {}
        for name, key in EMOJIS.items():
            emojis[name] = bot.get_emoji(key)
        patreon_button = discord.ui.Button(
            label="Become a Patron",
            style=ButtonStyle.red,
            emoji=emojis["patreon"],
            url="https://www.patreon.com/bePatron?u=9811418",
            row=2)
        github_button = discord.ui.Button(
            label="View source code.",
            style=ButtonStyle.blurple,
            emoji=emojis["github"],
            url="https://github.com/Maselkov/GW2Bot",
            row=1)
        kofi_button = discord.ui.Button(label="Buy me a cofee",
                                        style=ButtonStyle.link,
                                        url="https://ko-fi.com/maselkov",
                                        emoji=emojis["kofi"],
                                        row=2)
        privacy_policy = discord.ui.Button(
            label="Privacy policy.",
            style=ButtonStyle.blurple,
            url="https://gw2bot.info/privacy-policy",
            emoji="🔏",
            row=1)
        buttons = [patreon_button, github_button, kofi_button, privacy_policy]
        for button in buttons:
            self.add_item(button)


class Help(commands.Cog):
    """Control the bot's global settings"""

    def __init__(self, bot):

        self.bot: commands.AutoShardedBot = bot

    @app_commands.command()
    async def help(self, interaction: discord.Interaction):
        """Basic information about the bot"""
        embed = discord.Embed(title="View website",
                              color=self.bot.color,
                              url="https://gw2bot.info/")
        embed.add_field(
            name="Commands",
            value="To and use commands, "
            "type /, select GW2Bot icon on the left side, and scroll through "
            "the commands and descriptions. Alternatively, "
            "[view all the commands on the website](https://gw2bot.info/commands)"
        )
        await interaction.response.send_message(embed=embed,
                                                view=HelpView(self.bot))


async def setup(bot):
    cog = Help(bot)
    await bot.add_cog(cog)
