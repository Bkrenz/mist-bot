from discord import Embed
from ..apis.raidbots import RaidBots
from . import ItemColors, MIST_LOGO_URL, ISSUES_NOTE, FOOTER_DESC

class QELiveEmbed:

    @staticmethod
    def create(report_code, success, issue):
        # Setup the Basics
        t = 'Processed Successfully' if success else 'Report Error'
        embed = Embed(title=t, color=ItemColors.Common)

        embed.set_thumbnail(url= MIST_LOGO_URL)
        embed.set_author(name='Mist Guild Tools', url='https://github.com/Bkrenz/droptimizer-bot')
        embed.description = f'[QELive Link](https://questionablyepic.com/live/) \n'

        embed.description += f'Finished uploading report `{report_code}` to WowAudit.\n'
        embed.description += 'To view the WowAudit Wishlists, follow [this link](https://wowaudit.com/us/illidan/mist/mist/wishlists/overview).\n'

        if not success:
            embed.description += '\nYour report could not be processed due to the following error: '
            embed.description += f'```{issue}```'

        embed.description += f'\n{ISSUES_NOTE}'
            
        embed.set_footer(text=FOOTER_DESC, icon_url=MIST_LOGO_URL)

        return embed
    