from telegram.ext import Updater, MessageHandler, Filters

def convert_video_to_url(update, context):

    # Extract the video file from the update

    video_file = update.message.video

    # Get the video file's URL

    video_url = video_file.get_file().file_path

    # Send the URL back to the user

    update.message.reply_text(f"Video URL: {video_url}")

def main():

    # Create an instance of the Updater and pass your API token

    updater = Updater("6016828320:AAHcxeX0UQkx_kIzZkJ6uEuRvEgBJnRVDro", use_context=True)

    # Get the dispatcher to register handlers

    dispatcher = updater.dispatcher

    # Set up a handler to handle video messages

    video_handler = MessageHandler(Filters.video, convert_video_to_url)

    dispatcher.add_handler(video_handler)

    # Start the bot

    updater.start_polling()

    # Run the bot until you press Ctrl-C

    updater.idle()

if __name__ == '__main__':

    main()

