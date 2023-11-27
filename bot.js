const { Bot } = require("grammy");

const bot = new Bot("6916391004:AAGMpzQI9h2kNqdqoyXsOHpZfnYvlfSw-H0");

// Reply to any message with "Hi there!".
bot.on("message", (ctx) => ctx.reply("Hi there!"));

bot.start();
