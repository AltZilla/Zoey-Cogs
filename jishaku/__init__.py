from jishaku.cog import Jishaku


async def setup(bot):
    await bot.add_cog(Jishaku(bot=bot))
