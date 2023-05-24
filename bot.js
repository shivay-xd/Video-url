const { TelegramBot } = require('bottender');

const axios = require('axios');

const bot = new TelegramBot({

  accessToken: '6016828320:AAHcxeX0UQkx_kIzZkJ6uEuRvEgBJnRVDro',

});

bot.onEvent(async (context) => {

  if (context.event.isText) {

    // Handle text messages if needed

    return;

  }

  if (context.event.isVideo) {

    const { file_id } = context.event.message.video;

    try {

      const response = await bot.client.getFile({ file_id });

      const videoUrl = `https://api.telegram.org/file/bot${bot.accessToken}/${response.file_path}`;

      await context.sendText(`Video URL: ${videoUrl}`);

    } catch (error) {

      console.error(error);

    }

  }

});

bot.createLongPollingRuntime().start();

