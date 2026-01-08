import ctypes
import os
from pathlib import Path
from platform import system
from typing import Any

from .download import __GONEONIZE_VERSION__, download
from .utils.platform import generated_name

func_string = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)  # qr
func = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_bool)  # blocking
func_bytes = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int
)  # status
func_callback_bytes = ctypes.CFUNCTYPE(
    None, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int
)  # callback_bytes

func_callback_bytes2 = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_int
)  # callback_bytes


def load_goneonize():
    while True:
        try:
            gocode = ctypes.CDLL(f"{root_dir}/{generated_name()}")
            gocode.GetVersion.restype = ctypes.c_char_p
            if gocode.GetVersion().decode() != __GONEONIZE_VERSION__:
                raise Exception("Invalid Version")
            return gocode
        except OSError as e:
            print("e", e)
            raise e
        except Exception:
            download()


class Bytes(ctypes.Structure):
    ptr: int
    size: int
    _fields_ = [("ptr", ctypes.POINTER(ctypes.c_char)), ("size", ctypes.c_size_t)]

    def get_bytes(self):
        return ctypes.string_at(self.ptr, self.size)


if not os.environ.get("SPHINX"):
    if not (Path(__file__).parent / generated_name()).exists():
        download()
    file_ext = "dll" if system() == "Windows" else "so"
    root_dir = os.path.abspath(os.path.dirname(__file__))
    gocode = load_goneonize()

    gocode.Neonize.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        func_string,
        func_string,
        func_callback_bytes,
        func_callback_bytes2,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,  # automaticMessageRerequestFromPhone
    ]
    gocode.GetLIDFromPN.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetLIDFromPN.restype = ctypes.POINTER(Bytes)
    gocode.GetPNFromLID.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetPNFromLID.restype = ctypes.POINTER(Bytes)
    gocode.PinMessage.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.PinMessage.restype = ctypes.POINTER(Bytes)
    gocode.Upload.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.TestStruct.argtypes = []
    gocode.TestStruct.restype = ctypes.POINTER(Bytes)
    gocode.Upload.restype = ctypes.POINTER(Bytes)
    gocode.UploadNewsletter.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.UploadNewsletter.restype = ctypes.POINTER(Bytes)
    gocode.DownloadAny.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.DownloadAny.restype = ctypes.POINTER(Bytes)
    gocode.DownloadMediaWithPath.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.DownloadMediaWithPath.restype = ctypes.POINTER(Bytes)
    gocode.GetGroupInfo.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetGroupInfo.restype = ctypes.POINTER(Bytes)
    gocode.SetGroupPhoto.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.SetGroupPhoto.restype = ctypes.POINTER(Bytes)
    gocode.SetProfilePhoto.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.SetProfilePhoto.restype = ctypes.POINTER(Bytes)
    gocode.LeaveGroup.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.LeaveGroup.restype = ctypes.c_void_p
    gocode.SetGroupName.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.SetGroupName.restype = ctypes.c_void_p
    gocode.GetGroupInviteLink.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.GetGroupInviteLink.restype = ctypes.POINTER(Bytes)
    gocode.JoinGroupWithLink.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.JoinGroupWithLink.restype = ctypes.POINTER(Bytes)
    gocode.SendMessage.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.SendMessage.restype = ctypes.POINTER(Bytes)
    gocode.SendChatPresence.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.SendChatPresence.restype = ctypes.c_void_p
    gocode.BuildRevoke.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.BuildRevoke.restype = ctypes.POINTER(Bytes)
    gocode.CreateGroup.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.CreateGroup.restype = ctypes.POINTER(Bytes)
    gocode.GenerateMessageID.argtypes = [ctypes.c_char_p]
    gocode.GenerateMessageID.restype = ctypes.c_void_p
    gocode.IsOnWhatsApp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.IsOnWhatsApp.restype = ctypes.POINTER(Bytes)
    gocode.IsConnected.argtypes = [ctypes.c_char_p]
    gocode.IsConnected.restype = ctypes.c_bool
    gocode.IsLoggedIn.argtypes = [ctypes.c_char_p]
    gocode.IsLoggedIn.restype = ctypes.c_bool
    gocode.GetUserInfo.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetUserInfo.restype = ctypes.POINTER(Bytes)
    gocode.GetMe.argtypes = [ctypes.c_char_p]
    gocode.GetMe.restype = ctypes.POINTER(Bytes)
    gocode.BuildPollVoteCreation.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.BuildPollVoteCreation.restype = ctypes.POINTER(Bytes)
    gocode.BuildPollVote.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.BuildPollVote.restype = ctypes.POINTER(Bytes)
    gocode.BuildReaction.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
    gocode.BuildReaction.restype = ctypes.POINTER(Bytes)
    gocode.CreateNewsletter.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.CreateNewsletter.restype = ctypes.POINTER(Bytes)
    gocode.FollowNewsletter.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.FollowNewsletter.restype = ctypes.c_void_p
    gocode.GetBlocklist.argtypes = [ctypes.c_char_p]
    gocode.GetBlocklist.restype = ctypes.POINTER(Bytes)
    gocode.GetContactQRLink.argtypes = [ctypes.c_char_p, ctypes.c_bool]
    gocode.GetContactQRLink.restype = ctypes.POINTER(Bytes)
    gocode.GetGroupInfoFromInvite.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.GetGroupInfoFromInvite.restype = ctypes.POINTER(Bytes)
    gocode.GetGroupInfoFromLink.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.GetGroupInfoFromLink.restype = ctypes.POINTER(Bytes)
    gocode.GetGroupRequestParticipants.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.GetGroupRequestParticipants.restype = ctypes.POINTER(Bytes)
    gocode.GetJoinedGroups.argtypes = [ctypes.c_char_p]
    gocode.GetJoinedGroups.restype = ctypes.POINTER(Bytes)
    gocode.GetLinkedGroupsParticipants.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.GetLinkedGroupsParticipants.restype = ctypes.POINTER(Bytes)
    gocode.GetNewsletterInfo.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetNewsletterInfo.restype = ctypes.POINTER(Bytes)
    gocode.GetNewsletterInfoWithInvite.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.GetNewsletterInfoWithInvite.restype = ctypes.POINTER(Bytes)
    gocode.GetNewsletterMessageUpdate.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.GetNewsletterMessageUpdate.restype = ctypes.POINTER(Bytes)
    gocode.GetNewsletterMessages.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
    ]
    gocode.GetNewsletterMessages.restype = ctypes.POINTER(Bytes)
    gocode.GetPrivacySettings.argtypes = [ctypes.c_char_p]
    gocode.GetPrivacySettings.restype = ctypes.POINTER(Bytes)
    gocode.GetProfilePicture.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.GetProfilePicture.restype = ctypes.POINTER(Bytes)
    gocode.GetStatusPrivacy.argtypes = [ctypes.c_char_p]
    gocode.GetStatusPrivacy.restype = ctypes.POINTER(Bytes)
    gocode.GetSubGroups.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetSubGroups.restype = ctypes.POINTER(Bytes)
    gocode.GetSubscribedNewsletters.argtypes = [ctypes.c_char_p]
    gocode.GetSubscribedNewsletters.restype = ctypes.POINTER(Bytes)
    gocode.GetUserDevices.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetUserDevices.restype = ctypes.POINTER(Bytes)
    gocode.JoinGroupWithInvite.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.JoinGroupWithInvite.restype = ctypes.c_void_p
    gocode.LinkGroup.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.LinkGroup.restype = ctypes.c_void_p
    gocode.Logout.argtypes = [ctypes.c_char_p]
    gocode.Logout.restype = ctypes.c_void_p
    gocode.MarkRead.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.MarkRead.restype = ctypes.c_void_p
    gocode.NewsletterMarkViewed.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.NewsletterMarkViewed.restype = ctypes.c_void_p
    gocode.NewsletterSendReaction.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
    gocode.NewsletterSendReaction.restype = ctypes.c_void_p
    gocode.NewsletterSubscribeLiveUpdates.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.NewsletterSubscribeLiveUpdates.restype = ctypes.POINTER(Bytes)
    gocode.NewsletterToggleMute.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.NewsletterToggleMute.restype = ctypes.c_void_p
    gocode.Disconnect.argtypes = [ctypes.c_char_p]
    gocode.ResolveContactQRLink.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.ResolveContactQRLink.restype = ctypes.POINTER(Bytes)
    gocode.ResolveBusinessMessageLink.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.ResolveBusinessMessageLink.restype = ctypes.POINTER(Bytes)
    gocode.PairPhone.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.PairPhone.restype = ctypes.POINTER(Bytes)
    gocode.SendAppState.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.SendAppState.restype = ctypes.c_void_p
    gocode.FetchAppState.argtypes = [
        ctypes.c_char_p,  # id (session UUID)
        ctypes.c_char_p,  # patchName (WAPatchName as string)
        ctypes.c_bool,    # fullSync
        ctypes.c_bool,    # onlyIfNotSynced
    ]
    gocode.FetchAppState.restype = ctypes.c_void_p
    gocode.ClearAppState.argtypes = [
        ctypes.c_char_p,  # id (session UUID)
        ctypes.c_char_p,  # patchName (WAPatchName as string)
    ]
    gocode.ClearAppState.restype = ctypes.c_void_p
    gocode.SetDefaultDisappearingTimer.argtypes = [ctypes.c_char_p, ctypes.c_int64]
    gocode.SetDefaultDisappearingTimer.restype = ctypes.c_void_p
    gocode.SetDisappearingTimer.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int64,
        ctypes.c_int64,
    ]
    gocode.SetDisappearingTimer.restype = ctypes.c_void_p
    gocode.SetForceActiveDeliveryReceipts.argtypes = [ctypes.c_char_p, ctypes.c_bool]
    gocode.SetForceActiveDeliveryReceipts.restype = ctypes.c_void_p
    gocode.SetAutomaticMessageRerequestFromPhone.argtypes = [ctypes.c_char_p, ctypes.c_bool]
    gocode.SetAutomaticMessageRerequestFromPhone.restype = ctypes.c_void_p
    gocode.SetGroupAnnounce.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.SetGroupAnnounce.restype = ctypes.c_void_p
    gocode.SetGroupLocked.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.SetGroupLocked.restype = ctypes.c_void_p
    gocode.SetGroupTopic.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
    gocode.SetGroupTopic.restype = ctypes.c_void_p
    gocode.SetPrivacySetting.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
    gocode.SetPrivacySetting.restype = ctypes.POINTER(Bytes)
    gocode.SetPassive.argtypes = [ctypes.c_char_p, ctypes.c_bool]
    gocode.SetPassive.restype = ctypes.c_void_p
    gocode.SetStatusMessage.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.SetStatusMessage.restype = ctypes.c_void_p
    gocode.SubscribePresence.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.SubscribePresence.restype = ctypes.c_void_p
    gocode.UnfollowNewsletter.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.UnfollowNewsletter.restype = ctypes.c_void_p
    gocode.UnlinkGroup.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.UnlinkGroup.restype = ctypes.c_void_p
    gocode.UpdateBlocklist.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.UpdateBlocklist.restype = ctypes.POINTER(Bytes)
    gocode.UpdateGroupParticipants.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.UpdateGroupParticipants.restype = ctypes.POINTER(Bytes)
    gocode.GetMessageForRetry.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.GetMessageForRetry.restype = ctypes.POINTER(Bytes)
    gocode.PutPushName.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
    ]
    gocode.PutPushName.restype = ctypes.POINTER(Bytes)
    gocode.PutContactName.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
    gocode.PutContactName.restype = ctypes.c_void_p
    gocode.PutAllContactNames.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.PutAllContactNames.restype = ctypes.c_void_p
    gocode.GetContact.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetContact.restype = ctypes.POINTER(Bytes)
    gocode.GetAllContacts.argtypes = [ctypes.c_char_p]
    gocode.GetAllContacts.restype = ctypes.POINTER(Bytes)
    gocode.PutMutedUntil.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_float,
    ]
    gocode.PutMutedUntil.restype = ctypes.c_void_p
    gocode.PutPinned.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.PutPinned.restype = ctypes.c_void_p
    gocode.PutArchived.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_bool,
    ]
    gocode.PutArchived.restype = ctypes.c_void_p
    # ClearChat is now implemented in pure Python (aioze/client.py ChatSettingsStore.clear_chat)
    # No Go binding needed - uses send_app_state() directly
    gocode.GetChatSettings.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.GetChatSettings.restype = ctypes.POINTER(Bytes)
    gocode.GetAllDevices.argtypes = [ctypes.c_char_p, func_callback_bytes2]
    gocode.GetAllDevices.restype = ctypes.c_void_p
    gocode.SendFBMessage.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
    gocode.SendFBMessage.restype = ctypes.POINTER(Bytes)
    gocode.SendPresence.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    gocode.SendPresence.restype = ctypes.c_void_p
    gocode.DecryptPollVote.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    gocode.DecryptPollVote.restype = ctypes.POINTER(Bytes)
    gocode.Stop.argtypes = [ctypes.c_char_p]
    gocode.Stop.restype = ctypes.c_void_p
    gocode.StopAll.argtypes = []
    gocode.StopAll.restype = ctypes.c_void_p
    gocode.FreeBytesStruct.argtypes = [ctypes.POINTER(Bytes)]
    gocode.FreeBytesStruct.restype = None
    gocode.FreeString.argtypes = [ctypes.c_void_p]
    gocode.FreeString.restype = None
    # pprof profiling server for memory debugging
    gocode.StartPprof.argtypes = [ctypes.c_int]
    gocode.StartPprof.restype = ctypes.c_void_p

    # =========================================================================
    # MEMORY LEAK FIX WRAPPERS
    # =========================================================================
    # Go CGO functions return patterns that require different handling:
    # 1. *C.char returns: Use c_void_p + _wrap_cstring_return + FreeString
    # 2. *C.struct_BytesReturn: Use POINTER(Bytes) + _wrap_bytes_return + FreeBytesStruct
    # =========================================================================

    def _wrap_bytes_return(func):
        """Wrap Go function returning BytesReturn. Returns Python bytes, frees memory."""
        def wrapper(*args):
            bytes_ptr = func(*args)
            if not bytes_ptr:
                return b""
            result = bytes_ptr.contents.get_bytes()
            gocode.FreeBytesStruct(bytes_ptr)
            return result
        return wrapper

    def _wrap_cstring_return(func):
        """Wrap Go function returning *C.char. Returns Python string, frees memory."""
        def wrapper(*args):
            ptr = func(*args)  # c_void_p
            if not ptr:
                return ""
            result = ctypes.cast(ptr, ctypes.c_char_p).value.decode()
            gocode.FreeString(ptr)
            return result
        return wrapper

    # C string returns (Go returns *C.char via C.CString, freed with FreeString)
    gocode.PutContactName = _wrap_cstring_return(gocode.PutContactName)
    gocode.PutAllContactNames = _wrap_cstring_return(gocode.PutAllContactNames)
    gocode.PutMutedUntil = _wrap_cstring_return(gocode.PutMutedUntil)
    gocode.MarkRead = _wrap_cstring_return(gocode.MarkRead)
    gocode.SendChatPresence = _wrap_cstring_return(gocode.SendChatPresence)
    gocode.GenerateMessageID = _wrap_cstring_return(gocode.GenerateMessageID)
    gocode.PutPinned = _wrap_cstring_return(gocode.PutPinned)
    gocode.PutArchived = _wrap_cstring_return(gocode.PutArchived)
    gocode.SetGroupName = _wrap_cstring_return(gocode.SetGroupName)
    gocode.LeaveGroup = _wrap_cstring_return(gocode.LeaveGroup)
    gocode.LinkGroup = _wrap_cstring_return(gocode.LinkGroup)
    gocode.Logout = _wrap_cstring_return(gocode.Logout)
    gocode.NewsletterMarkViewed = _wrap_cstring_return(gocode.NewsletterMarkViewed)
    gocode.NewsletterSendReaction = _wrap_cstring_return(gocode.NewsletterSendReaction)
    gocode.NewsletterToggleMute = _wrap_cstring_return(gocode.NewsletterToggleMute)
    gocode.SendAppState = _wrap_cstring_return(gocode.SendAppState)
    gocode.FetchAppState = _wrap_cstring_return(gocode.FetchAppState)
    gocode.ClearAppState = _wrap_cstring_return(gocode.ClearAppState)
    gocode.SetDefaultDisappearingTimer = _wrap_cstring_return(gocode.SetDefaultDisappearingTimer)
    gocode.SetDisappearingTimer = _wrap_cstring_return(gocode.SetDisappearingTimer)
    gocode.SetGroupAnnounce = _wrap_cstring_return(gocode.SetGroupAnnounce)
    gocode.SetGroupLocked = _wrap_cstring_return(gocode.SetGroupLocked)
    gocode.SetGroupTopic = _wrap_cstring_return(gocode.SetGroupTopic)
    gocode.SetPassive = _wrap_cstring_return(gocode.SetPassive)
    gocode.SetStatusMessage = _wrap_cstring_return(gocode.SetStatusMessage)
    gocode.SubscribePresence = _wrap_cstring_return(gocode.SubscribePresence)
    gocode.UnfollowNewsletter = _wrap_cstring_return(gocode.UnfollowNewsletter)
    gocode.UnlinkGroup = _wrap_cstring_return(gocode.UnlinkGroup)
    gocode.FollowNewsletter = _wrap_cstring_return(gocode.FollowNewsletter)
    gocode.SendPresence = _wrap_cstring_return(gocode.SendPresence)
    gocode.SetPrivacySetting = _wrap_bytes_return(gocode.SetPrivacySetting)
    gocode.JoinGroupWithInvite = _wrap_cstring_return(gocode.JoinGroupWithInvite)
    gocode.GetAllDevices = _wrap_cstring_return(gocode.GetAllDevices)

    # Bytes returns (protobuf data - uses BytesReturn struct, freed with FreeBytesStruct)
    gocode.JoinGroupWithLink = _wrap_bytes_return(gocode.JoinGroupWithLink)
    gocode.SendMessage = _wrap_bytes_return(gocode.SendMessage)
    gocode.GetGroupInfo = _wrap_bytes_return(gocode.GetGroupInfo)
    gocode.GetMe = _wrap_bytes_return(gocode.GetMe)
    gocode.IsOnWhatsApp = _wrap_bytes_return(gocode.IsOnWhatsApp)
    gocode.GetContact = _wrap_bytes_return(gocode.GetContact)
    gocode.GetAllContacts = _wrap_bytes_return(gocode.GetAllContacts)
    gocode.PutPushName = _wrap_bytes_return(gocode.PutPushName)
    gocode.GetChatSettings = _wrap_bytes_return(gocode.GetChatSettings)
    gocode.BuildPollVoteCreation = _wrap_bytes_return(gocode.BuildPollVoteCreation)
    gocode.BuildPollVote = _wrap_bytes_return(gocode.BuildPollVote)
    gocode.BuildReaction = _wrap_bytes_return(gocode.BuildReaction)
    gocode.BuildRevoke = _wrap_bytes_return(gocode.BuildRevoke)
    gocode.Upload = _wrap_bytes_return(gocode.Upload)
    gocode.DownloadAny = _wrap_bytes_return(gocode.DownloadAny)
    gocode.DownloadMediaWithPath = _wrap_bytes_return(gocode.DownloadMediaWithPath)
    gocode.GetUserInfo = _wrap_bytes_return(gocode.GetUserInfo)
    gocode.GetGroupInfoFromLink = _wrap_bytes_return(gocode.GetGroupInfoFromLink)
    gocode.GetGroupInfoFromInvite = _wrap_bytes_return(gocode.GetGroupInfoFromInvite)
    gocode.SetGroupPhoto = _wrap_bytes_return(gocode.SetGroupPhoto)
    gocode.SetProfilePhoto = _wrap_bytes_return(gocode.SetProfilePhoto)
    gocode.GetLIDFromPN = _wrap_bytes_return(gocode.GetLIDFromPN)
    gocode.GetPNFromLID = _wrap_bytes_return(gocode.GetPNFromLID)
    gocode.PinMessage = _wrap_bytes_return(gocode.PinMessage)
    gocode.GetGroupInviteLink = _wrap_bytes_return(gocode.GetGroupInviteLink)
    gocode.NewsletterSubscribeLiveUpdates = _wrap_bytes_return(gocode.NewsletterSubscribeLiveUpdates)
    gocode.ResolveBusinessMessageLink = _wrap_bytes_return(gocode.ResolveBusinessMessageLink)
    gocode.ResolveContactQRLink = _wrap_bytes_return(gocode.ResolveContactQRLink)
    gocode.UpdateBlocklist = _wrap_bytes_return(gocode.UpdateBlocklist)
    gocode.UpdateGroupParticipants = _wrap_bytes_return(gocode.UpdateGroupParticipants)
    gocode.UploadNewsletter = _wrap_bytes_return(gocode.UploadNewsletter)
    gocode.CreateGroup = _wrap_bytes_return(gocode.CreateGroup)
    gocode.GetGroupRequestParticipants = _wrap_bytes_return(gocode.GetGroupRequestParticipants)
    gocode.GetJoinedGroups = _wrap_bytes_return(gocode.GetJoinedGroups)
    gocode.CreateNewsletter = _wrap_bytes_return(gocode.CreateNewsletter)
    gocode.GetNewsletterInfoWithInvite = _wrap_bytes_return(gocode.GetNewsletterInfoWithInvite)
    gocode.GetNewsletterMessageUpdate = _wrap_bytes_return(gocode.GetNewsletterMessageUpdate)
    gocode.GetNewsletterMessages = _wrap_bytes_return(gocode.GetNewsletterMessages)
    gocode.GetPrivacySettings = _wrap_bytes_return(gocode.GetPrivacySettings)
    gocode.GetProfilePicture = _wrap_bytes_return(gocode.GetProfilePicture)
    gocode.GetStatusPrivacy = _wrap_bytes_return(gocode.GetStatusPrivacy)
    gocode.GetSubGroups = _wrap_bytes_return(gocode.GetSubGroups)
    gocode.GetSubscribedNewsletters = _wrap_bytes_return(gocode.GetSubscribedNewsletters)
    gocode.GetUserDevices = _wrap_bytes_return(gocode.GetUserDevices)
    gocode.GetBlocklist = _wrap_bytes_return(gocode.GetBlocklist)
    gocode.GetContactQRLink = _wrap_bytes_return(gocode.GetContactQRLink)
    gocode.GetLinkedGroupsParticipants = _wrap_bytes_return(gocode.GetLinkedGroupsParticipants)
    gocode.GetNewsletterInfo = _wrap_bytes_return(gocode.GetNewsletterInfo)
    gocode.PairPhone = _wrap_bytes_return(gocode.PairPhone)
    gocode.GetMessageForRetry = _wrap_bytes_return(gocode.GetMessageForRetry)
    gocode.SendFBMessage = _wrap_bytes_return(gocode.SendFBMessage)
    gocode.DecryptPollVote = _wrap_bytes_return(gocode.DecryptPollVote)

else:
    gocode: Any = object()


def free_bytes(bytes_ptr: ctypes._Pointer):
    """Free memory allocated by Go BytesReturn."""
    gocode.FreeBytesStruct(bytes_ptr)
