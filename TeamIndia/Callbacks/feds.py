from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from TeamIndia.__main__ import *


# Buttons Function for Federation module


def india_fed_admin_callback(update, context):
    query = update.callback_query
    if query.data == "indiafedadmin_":
        query.message.edit_text(
            text="""**FED ADMINS**

The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.            
            

**Commands:**

- /fban: Bans a user from the current chat's federation
- /unfban: Unbans a user from the current chat's federation
- /feddemoteme <fedID>: Demote yourself from a fed.
- /myfeds: List all feds you are an admin in.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Fedration)")
                 ]
                ]
            ),
        )

def india_fed_owner_callback(update, context):
    query = update.callback_query
    if query.data == "indiafedowner_":
        query.message.edit_text(
            text=""" **Federation Owner Commands** 
These are the list of available fed owner commands. To run these, you have to own the current federation.

**Owner Commands:**
- /newfed <fedname>: Creates a new federation with the given name. Only one federation per user.
- /renamefed <fedname>: Rename your federation.
- /delfed: Deletes your federation, and any information related to it. Will not unban any banned users.
- /fedtransfer <reply/username/mention/userid>: Transfer your federation to another user.
- /fedpromote: Promote a user to fedadmin in your fed. To avoid unwanted fedadmin, the user will get a message to confirm this.
- /feddemote: Demote a federation admin in your fed.
- /fednotif <yes/no/on/off>: Whether or not to receive PM notifications of every fed action.
- /fedreason <yes/no/on/off>: Whether or not fedbans should require a reason.
- /subfed <FedId>: Subscribe your federation to another. Users banned in the subscribed fed will also be banned in this one.
Note: This does not affect your banlist. You just inherit any bans.
- /unsubfed <FedId>: Unsubscribes your federation from another. Bans from the other fed will no longer take effect.
- /fedexport <csv/minicsv/json/human>: Get the list of currently banned users. Default output is CSV.
- /fedimport: Import a list of banned users.
- /setfedlog: Sets the current chat as the federation log. All federation events will be logged here.
- /unsetfedlog: Unset the federation log. Events will no longer be logged.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Fedration)")
                 ]
                ]
            ),
        )

def india_fed_user_callback(update, context):
    query = update.callback_query
    if query.data == "indiafeduser_":
        query.message.edit_text(
            text=""" **User Commands**
            
These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.

**Commands:**
- /fedinfo <FedID>: Information about a federation.
- /fedadmins <FedID>: List the admins in a federation.
- /fedsubs <FedID>: List all federations your federation is subscribed to.
- /joinfed <FedID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
- /leavefed: Leave the current federation. Only chat owners can do this.
- /fedstat <user ID>: List all the federations that you, or another user, have been banned in.
- /fedstat <user ID> <FedID>: Gives information about a user's ban in a federation.
- /chatfed: Information about the federation the current chat is in.
- /quietfed <yes/no/on/off>: Whether or not to send ban notifications when fedbanned users join the chat.         
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Fedration)")
                 ]
                ]
            ),
        )

fed_admin_callback_handler = CallbackQueryHandler(fed_admin_callback_handler, pattern=r"indiafedadmin_", run_async=True)
fed_owner_callback_handler = CallbackQueryHandler(fed_owner_callback_handler, pattern=r"indiafedowner_", run_async=True)
fed_user_callback_handler = CallbackQueryHandler(fed_user_callback_handler, pattern=r"indiafeduser_", run_async=True)

