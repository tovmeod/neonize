from waVnameCert import WAWebProtobufsVnameCert_pb2 as _WAWebProtobufsVnameCert_pb2
from waE2E import WAWebProtobufsE2E_pb2 as _WAWebProtobufsE2E_pb2
from waWeb import WAWebProtobufsWeb_pb2 as _WAWebProtobufsWeb_pb2
from waSyncAction import WASyncAction_pb2 as _WASyncAction_pb2
from waHistorySync import WAWebProtobufsHistorySync_pb2 as _WAWebProtobufsHistorySync_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ADMIN: NewsletterRole
BAD_USER_AGENT: ConnectFailureReason
CLIENT_OUTDATED: ConnectFailureReason
DESCRIPTOR: _descriptor.FileDescriptor
EXPERIMENTAL: ConnectFailureReason
GENERIC: ConnectFailureReason
GUEST: NewsletterRole
INTERNAL_SERVER_ERROR: ConnectFailureReason
LID: AddressingMode
LOGGED_OUT: ConnectFailureReason
MAIN_DEVICE_GONE: ConnectFailureReason
OFF: NewsletterMuteState
ON: NewsletterMuteState
OWNER: NewsletterRole
PN: AddressingMode
SERVICE_UNAVAILABLE: ConnectFailureReason
SUBSCRIBER: NewsletterRole
TEMP_BANNED: ConnectFailureReason
UNKNOWN_LOGOUT: ConnectFailureReason

class AppStateSyncComplete(_message.Message):
    __slots__ = ["Name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Name: _Optional[str] = ...) -> None: ...

class ArrayString(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...

class BasicCallMeta(_message.Message):
    __slots__ = ["callCreator", "callCreatorAlt", "callID", "timestamp"]
    CALLCREATORALT_FIELD_NUMBER: _ClassVar[int]
    CALLCREATOR_FIELD_NUMBER: _ClassVar[int]
    CALLID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    callCreator: JID
    callCreatorAlt: JID
    callID: str
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ..., callCreator: _Optional[_Union[JID, _Mapping]] = ..., callCreatorAlt: _Optional[_Union[JID, _Mapping]] = ..., callID: _Optional[str] = ..., **kwargs) -> None: ...

class Blocklist(_message.Message):
    __slots__ = ["DHash", "JIDs"]
    DHASH_FIELD_NUMBER: _ClassVar[int]
    DHash: str
    JIDS_FIELD_NUMBER: _ClassVar[int]
    JIDs: _containers.RepeatedCompositeFieldContainer[JID]
    def __init__(self, DHash: _Optional[str] = ..., JIDs: _Optional[_Iterable[_Union[JID, _Mapping]]] = ...) -> None: ...

class BlocklistChange(_message.Message):
    __slots__ = ["BlockAction", "JID"]
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLOCK: BlocklistChange.Action
    BLOCKACTION_FIELD_NUMBER: _ClassVar[int]
    BlockAction: BlocklistChange.Action
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    UNBLOCK: BlocklistChange.Action
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., BlockAction: _Optional[_Union[BlocklistChange.Action, str]] = ...) -> None: ...

class BlocklistEvent(_message.Message):
    __slots__ = ["Action", "Changes", "DHASH", "PrevDHash"]
    class Actions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTION_FIELD_NUMBER: _ClassVar[int]
    Action: BlocklistEvent.Actions
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    Changes: _containers.RepeatedCompositeFieldContainer[BlocklistChange]
    DEFAULT: BlocklistEvent.Actions
    DHASH: str
    DHASH_FIELD_NUMBER: _ClassVar[int]
    MODIFY: BlocklistEvent.Actions
    PREVDHASH_FIELD_NUMBER: _ClassVar[int]
    PrevDHash: str
    def __init__(self, Action: _Optional[_Union[BlocklistEvent.Actions, str]] = ..., DHASH: _Optional[str] = ..., PrevDHash: _Optional[str] = ..., Changes: _Optional[_Iterable[_Union[BlocklistChange, _Mapping]]] = ...) -> None: ...

class BroadcastRecipient(_message.Message):
    __slots__ = ["LID", "PN"]
    LID: JID
    LID_FIELD_NUMBER: _ClassVar[int]
    PN: JID
    PN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, LID: _Optional[_Union[JID, _Mapping]] = ..., PN: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class BuildMessageReturnFunction(_message.Message):
    __slots__ = ["Error", "Message"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: _WAWebProtobufsE2E_pb2.Message
    def __init__(self, Error: _Optional[str] = ..., Message: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ...) -> None: ...

class BuildPollVoteReturnFunction(_message.Message):
    __slots__ = ["Error", "PollVote"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    POLLVOTE_FIELD_NUMBER: _ClassVar[int]
    PollVote: _WAWebProtobufsE2E_pb2.Message
    def __init__(self, PollVote: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class BusinessMessageLinkTarget(_message.Message):
    __slots__ = ["IsSigned", "JID", "Message", "PushName", "VerifiedLevel", "VerifiedName"]
    ISSIGNED_FIELD_NUMBER: _ClassVar[int]
    IsSigned: bool
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: str
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    PushName: str
    VERIFIEDLEVEL_FIELD_NUMBER: _ClassVar[int]
    VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
    VerifiedLevel: str
    VerifiedName: str
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., PushName: _Optional[str] = ..., VerifiedName: _Optional[str] = ..., IsSigned: bool = ..., VerifiedLevel: _Optional[str] = ..., Message: _Optional[str] = ...) -> None: ...

class CallAccept(_message.Message):
    __slots__ = ["basicCallMeta", "callRemoteMeta", "data"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    CALLREMOTEMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    callRemoteMeta: CallRemoteMeta
    data: Node
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., callRemoteMeta: _Optional[_Union[CallRemoteMeta, _Mapping]] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallOffer(_message.Message):
    __slots__ = ["basicCallMeta", "callRemoteMeta", "data"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    CALLREMOTEMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    callRemoteMeta: CallRemoteMeta
    data: Node
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., callRemoteMeta: _Optional[_Union[CallRemoteMeta, _Mapping]] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallOfferNotice(_message.Message):
    __slots__ = ["basicCallMeta", "data", "media", "type"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    data: Node
    media: str
    type: str
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., media: _Optional[str] = ..., type: _Optional[str] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallPreAccept(_message.Message):
    __slots__ = ["basicCallMeta", "callRemoteMeta", "data"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    CALLREMOTEMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    callRemoteMeta: CallRemoteMeta
    data: Node
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., callRemoteMeta: _Optional[_Union[CallRemoteMeta, _Mapping]] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallRelayLatency(_message.Message):
    __slots__ = ["basicCallMeta", "data"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    data: Node
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallRemoteMeta(_message.Message):
    __slots__ = ["remotePlatform", "remoteVersion"]
    REMOTEPLATFORM_FIELD_NUMBER: _ClassVar[int]
    REMOTEVERSION_FIELD_NUMBER: _ClassVar[int]
    remotePlatform: str
    remoteVersion: str
    def __init__(self, remotePlatform: _Optional[str] = ..., remoteVersion: _Optional[str] = ...) -> None: ...

class CallTerminate(_message.Message):
    __slots__ = ["basicCallMeta", "data", "reason"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    data: Node
    reason: str
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., reason: _Optional[str] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class CallTransport(_message.Message):
    __slots__ = ["basicCallMeta", "callRemoteMeta", "data"]
    BASICCALLMETA_FIELD_NUMBER: _ClassVar[int]
    CALLREMOTEMETA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    basicCallMeta: BasicCallMeta
    callRemoteMeta: CallRemoteMeta
    data: Node
    def __init__(self, basicCallMeta: _Optional[_Union[BasicCallMeta, _Mapping]] = ..., callRemoteMeta: _Optional[_Union[CallRemoteMeta, _Mapping]] = ..., data: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class ChatPresence(_message.Message):
    __slots__ = ["Media", "MessageSource", "State"]
    class ChatPresence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ChatPresenceMedia(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUDIO: ChatPresence.ChatPresenceMedia
    COMPOSING: ChatPresence.ChatPresence
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    MESSAGESOURCE_FIELD_NUMBER: _ClassVar[int]
    Media: ChatPresence.ChatPresenceMedia
    MessageSource: MessageSource
    PAUSED: ChatPresence.ChatPresence
    STATE_FIELD_NUMBER: _ClassVar[int]
    State: ChatPresence.ChatPresence
    TEXT: ChatPresence.ChatPresenceMedia
    def __init__(self, MessageSource: _Optional[_Union[MessageSource, _Mapping]] = ..., State: _Optional[_Union[ChatPresence.ChatPresence, str]] = ..., Media: _Optional[_Union[ChatPresence.ChatPresenceMedia, str]] = ...) -> None: ...

class ClientOutdated(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConnectFailure(_message.Message):
    __slots__ = ["Message", "Raw", "Reason"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: str
    RAW_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    Raw: Node
    Reason: ConnectFailureReason
    def __init__(self, Reason: _Optional[_Union[ConnectFailureReason, str]] = ..., Message: _Optional[str] = ..., Raw: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class Connected(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ["Info", "JID"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    Info: ContactInfo
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., Info: _Optional[_Union[ContactInfo, _Mapping]] = ...) -> None: ...

class ContactEntry(_message.Message):
    __slots__ = ["FirstName", "FullName", "JID"]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    FullName: str
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., FirstName: _Optional[str] = ..., FullName: _Optional[str] = ...) -> None: ...

class ContactEntryArray(_message.Message):
    __slots__ = ["ContactEntry"]
    CONTACTENTRY_FIELD_NUMBER: _ClassVar[int]
    ContactEntry: _containers.RepeatedCompositeFieldContainer[ContactEntry]
    def __init__(self, ContactEntry: _Optional[_Iterable[_Union[ContactEntry, _Mapping]]] = ...) -> None: ...

class ContactInfo(_message.Message):
    __slots__ = ["BusinessName", "FirstName", "Found", "FullName", "PushName", "RedactedPhone"]
    BUSINESSNAME_FIELD_NUMBER: _ClassVar[int]
    BusinessName: str
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    Found: bool
    FullName: str
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    PushName: str
    REDACTEDPHONE_FIELD_NUMBER: _ClassVar[int]
    RedactedPhone: str
    def __init__(self, Found: bool = ..., FirstName: _Optional[str] = ..., FullName: _Optional[str] = ..., PushName: _Optional[str] = ..., BusinessName: _Optional[str] = ..., RedactedPhone: _Optional[str] = ...) -> None: ...

class ContactQRLinkTarget(_message.Message):
    __slots__ = ["JID", "PushName", "Type"]
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    PushName: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: str
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., Type: _Optional[str] = ..., PushName: _Optional[str] = ...) -> None: ...

class ContactsGetAllContactsReturnFunction(_message.Message):
    __slots__ = ["Contact", "Error"]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    Contact: _containers.RepeatedCompositeFieldContainer[Contact]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, Contact: _Optional[_Iterable[_Union[Contact, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class ContactsGetContactReturnFunction(_message.Message):
    __slots__ = ["ContactInfo", "Error"]
    CONTACTINFO_FIELD_NUMBER: _ClassVar[int]
    ContactInfo: ContactInfo
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, ContactInfo: _Optional[_Union[ContactInfo, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class ContactsPutPushNameReturnFunction(_message.Message):
    __slots__ = ["Error", "PreviousName", "Status"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    PREVIOUSNAME_FIELD_NUMBER: _ClassVar[int]
    PreviousName: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Status: bool
    def __init__(self, Status: bool = ..., PreviousName: _Optional[str] = ..., Error: _Optional[str] = ...) -> None: ...

class CreateNewsLetterReturnFunction(_message.Message):
    __slots__ = ["Error", "NewsletterMetadata"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    NEWSLETTERMETADATA_FIELD_NUMBER: _ClassVar[int]
    NewsletterMetadata: NewsletterMetadata
    def __init__(self, NewsletterMetadata: _Optional[_Union[NewsletterMetadata, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class CreateNewsletterParams(_message.Message):
    __slots__ = ["Description", "Name", "Picture"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    Description: str
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    Picture: bytes
    def __init__(self, Name: _Optional[str] = ..., Description: _Optional[str] = ..., Picture: _Optional[bytes] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["BussinessName", "Initialized", "JID", "LID", "Platform", "PushName"]
    BUSSINESSNAME_FIELD_NUMBER: _ClassVar[int]
    BussinessName: str
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    Initialized: bool
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    LID: JID
    LID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    Platform: str
    PushName: str
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., LID: _Optional[_Union[JID, _Mapping]] = ..., Platform: _Optional[str] = ..., BussinessName: _Optional[str] = ..., PushName: _Optional[str] = ..., Initialized: bool = ...) -> None: ...

class DeviceSentMeta(_message.Message):
    __slots__ = ["DestinationJID", "Phash"]
    DESTINATIONJID_FIELD_NUMBER: _ClassVar[int]
    DestinationJID: str
    PHASH_FIELD_NUMBER: _ClassVar[int]
    Phash: str
    def __init__(self, DestinationJID: _Optional[str] = ..., Phash: _Optional[str] = ...) -> None: ...

class Disconnected(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class DownloadReturnFunction(_message.Message):
    __slots__ = ["Binary", "Error"]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    Binary: bytes
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, Binary: _Optional[bytes] = ..., Error: _Optional[str] = ...) -> None: ...

class GetBlocklistReturnFunction(_message.Message):
    __slots__ = ["Blocklist", "Error"]
    BLOCKLIST_FIELD_NUMBER: _ClassVar[int]
    Blocklist: Blocklist
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, Blocklist: _Optional[_Union[Blocklist, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetContactQRLinkReturnFunction(_message.Message):
    __slots__ = ["Error", "Link"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    LINK_FIELD_NUMBER: _ClassVar[int]
    Link: str
    def __init__(self, Link: _Optional[str] = ..., Error: _Optional[str] = ...) -> None: ...

class GetGroupInfoReturnFunction(_message.Message):
    __slots__ = ["Error", "GroupInfo"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    GROUPINFO_FIELD_NUMBER: _ClassVar[int]
    GroupInfo: GroupInfo
    def __init__(self, GroupInfo: _Optional[_Union[GroupInfo, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetGroupInviteLinkReturnFunction(_message.Message):
    __slots__ = ["Error", "InviteLink"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    INVITELINK_FIELD_NUMBER: _ClassVar[int]
    InviteLink: str
    def __init__(self, InviteLink: _Optional[str] = ..., Error: _Optional[str] = ...) -> None: ...

class GetGroupRequestParticipantsReturnFunction(_message.Message):
    __slots__ = ["Error", "Participants"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    Participants: _containers.RepeatedCompositeFieldContainer[GroupParticipantRequest]
    def __init__(self, Participants: _Optional[_Iterable[_Union[GroupParticipantRequest, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetJIDFromStoreReturnFunction(_message.Message):
    __slots__ = ["Error", "Jid"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    JID_FIELD_NUMBER: _ClassVar[int]
    Jid: JID
    def __init__(self, Error: _Optional[str] = ..., Jid: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class GetJoinedGroupsReturnFunction(_message.Message):
    __slots__ = ["Error", "Group"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    GROUP_FIELD_NUMBER: _ClassVar[int]
    Group: _containers.RepeatedCompositeFieldContainer[GroupInfo]
    def __init__(self, Group: _Optional[_Iterable[_Union[GroupInfo, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetMessageForRetryReturnFunction(_message.Message):
    __slots__ = ["Error", "Message", "isEmpty"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    ISEMPTY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: _WAWebProtobufsE2E_pb2.Message
    isEmpty: bool
    def __init__(self, isEmpty: bool = ..., Message: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetNewsletterMessageUpdateReturnFunction(_message.Message):
    __slots__ = ["Error", "NewsletterMessage"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    NEWSLETTERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    NewsletterMessage: _containers.RepeatedCompositeFieldContainer[NewsletterMessage]
    def __init__(self, NewsletterMessage: _Optional[_Iterable[_Union[NewsletterMessage, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetProfilePictureParams(_message.Message):
    __slots__ = ["ExistingID", "IsCommunity", "Preview"]
    EXISTINGID_FIELD_NUMBER: _ClassVar[int]
    ExistingID: str
    ISCOMMUNITY_FIELD_NUMBER: _ClassVar[int]
    IsCommunity: bool
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    Preview: bool
    def __init__(self, Preview: bool = ..., ExistingID: _Optional[str] = ..., IsCommunity: bool = ...) -> None: ...

class GetProfilePictureReturnFunction(_message.Message):
    __slots__ = ["Error", "Picture"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    Picture: ProfilePictureInfo
    def __init__(self, Picture: _Optional[_Union[ProfilePictureInfo, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetStatusPrivacyReturnFunction(_message.Message):
    __slots__ = ["Error", "StatusPrivacy"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    STATUSPRIVACY_FIELD_NUMBER: _ClassVar[int]
    StatusPrivacy: _containers.RepeatedCompositeFieldContainer[StatusPrivacy]
    def __init__(self, StatusPrivacy: _Optional[_Iterable[_Union[StatusPrivacy, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetSubGroupsReturnFunction(_message.Message):
    __slots__ = ["Error", "GroupLinkTarget"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    GROUPLINKTARGET_FIELD_NUMBER: _ClassVar[int]
    GroupLinkTarget: _containers.RepeatedCompositeFieldContainer[GroupLinkTarget]
    def __init__(self, GroupLinkTarget: _Optional[_Iterable[_Union[GroupLinkTarget, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetSubscribedNewslettersReturnFunction(_message.Message):
    __slots__ = ["Error", "Newsletter"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    Newsletter: _containers.RepeatedCompositeFieldContainer[NewsletterMetadata]
    def __init__(self, Newsletter: _Optional[_Iterable[_Union[NewsletterMetadata, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetUserDevicesreturnFunction(_message.Message):
    __slots__ = ["Error", "JID"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    JID: _containers.RepeatedCompositeFieldContainer[JID]
    JID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JID: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetUserInfoReturnFunction(_message.Message):
    __slots__ = ["Error", "UsersInfo"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    USERSINFO_FIELD_NUMBER: _ClassVar[int]
    UsersInfo: _containers.RepeatedCompositeFieldContainer[GetUserInfoSingleReturnFunction]
    def __init__(self, UsersInfo: _Optional[_Iterable[_Union[GetUserInfoSingleReturnFunction, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class GetUserInfoSingleReturnFunction(_message.Message):
    __slots__ = ["JID", "UserInfo"]
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    USERINFO_FIELD_NUMBER: _ClassVar[int]
    UserInfo: UserInfo
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., UserInfo: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class GroupAnnounce(_message.Message):
    __slots__ = ["AnnounceVersionID", "IsAnnounce"]
    ANNOUNCEVERSIONID_FIELD_NUMBER: _ClassVar[int]
    AnnounceVersionID: str
    ISANNOUNCE_FIELD_NUMBER: _ClassVar[int]
    IsAnnounce: bool
    def __init__(self, IsAnnounce: bool = ..., AnnounceVersionID: _Optional[str] = ...) -> None: ...

class GroupDelete(_message.Message):
    __slots__ = ["Deleted", "DeletedReason"]
    DELETEDREASON_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    Deleted: bool
    DeletedReason: str
    def __init__(self, Deleted: bool = ..., DeletedReason: _Optional[str] = ...) -> None: ...

class GroupEphemeral(_message.Message):
    __slots__ = ["DisappearingTimer", "IsEphemeral"]
    DISAPPEARINGTIMER_FIELD_NUMBER: _ClassVar[int]
    DisappearingTimer: int
    ISEPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    IsEphemeral: bool
    def __init__(self, IsEphemeral: bool = ..., DisappearingTimer: _Optional[int] = ...) -> None: ...

class GroupIncognito(_message.Message):
    __slots__ = ["IsIncognito"]
    ISINCOGNITO_FIELD_NUMBER: _ClassVar[int]
    IsIncognito: bool
    def __init__(self, IsIncognito: bool = ...) -> None: ...

class GroupInfo(_message.Message):
    __slots__ = ["GroupAnnounce", "GroupCreated", "GroupEphemeral", "GroupIncognito", "GroupIsDefaultSub", "GroupLinkedParent", "GroupLocked", "GroupName", "GroupParent", "GroupTopic", "JID", "OwnerJID", "OwnerPN", "ParticipantVersionID", "Participants"]
    class GroupMemberAddMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    GROUPANNOUNCE_FIELD_NUMBER: _ClassVar[int]
    GROUPCREATED_FIELD_NUMBER: _ClassVar[int]
    GROUPEPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    GROUPINCOGNITO_FIELD_NUMBER: _ClassVar[int]
    GROUPISDEFAULTSUB_FIELD_NUMBER: _ClassVar[int]
    GROUPLINKEDPARENT_FIELD_NUMBER: _ClassVar[int]
    GROUPLOCKED_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    GROUPPARENT_FIELD_NUMBER: _ClassVar[int]
    GROUPTOPIC_FIELD_NUMBER: _ClassVar[int]
    GroupAnnounce: GroupAnnounce
    GroupCreated: float
    GroupEphemeral: GroupEphemeral
    GroupIncognito: GroupIncognito
    GroupIsDefaultSub: GroupIsDefaultSub
    GroupLinkedParent: GroupLinkedParent
    GroupLocked: GroupLocked
    GroupMemberAddModeAdmin: GroupInfo.GroupMemberAddMode
    GroupName: GroupName
    GroupParent: GroupParent
    GroupTopic: GroupTopic
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    OWNERJID_FIELD_NUMBER: _ClassVar[int]
    OWNERPN_FIELD_NUMBER: _ClassVar[int]
    OwnerJID: JID
    OwnerPN: JID
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTVERSIONID_FIELD_NUMBER: _ClassVar[int]
    ParticipantVersionID: str
    Participants: _containers.RepeatedCompositeFieldContainer[GroupParticipant]
    def __init__(self, OwnerJID: _Optional[_Union[JID, _Mapping]] = ..., JID: _Optional[_Union[JID, _Mapping]] = ..., OwnerPN: _Optional[_Union[JID, _Mapping]] = ..., GroupName: _Optional[_Union[GroupName, _Mapping]] = ..., GroupTopic: _Optional[_Union[GroupTopic, _Mapping]] = ..., GroupLocked: _Optional[_Union[GroupLocked, _Mapping]] = ..., GroupAnnounce: _Optional[_Union[GroupAnnounce, _Mapping]] = ..., GroupEphemeral: _Optional[_Union[GroupEphemeral, _Mapping]] = ..., GroupIncognito: _Optional[_Union[GroupIncognito, _Mapping]] = ..., GroupParent: _Optional[_Union[GroupParent, _Mapping]] = ..., GroupLinkedParent: _Optional[_Union[GroupLinkedParent, _Mapping]] = ..., GroupIsDefaultSub: _Optional[_Union[GroupIsDefaultSub, _Mapping]] = ..., GroupCreated: _Optional[float] = ..., ParticipantVersionID: _Optional[str] = ..., Participants: _Optional[_Iterable[_Union[GroupParticipant, _Mapping]]] = ...) -> None: ...

class GroupInfoEvent(_message.Message):
    __slots__ = ["Announce", "Delete", "Demote", "Ephemeral", "JID", "Join", "JoinReason", "Leave", "Link", "Locked", "Name", "NewInviteLink", "Notify", "ParticipantVersionID", "PrevParticipantsVersionID", "Promote", "Sender", "Timestamp", "Topic", "UnknownChanges", "Unlink"]
    ANNOUNCE_FIELD_NUMBER: _ClassVar[int]
    Announce: GroupAnnounce
    DELETE_FIELD_NUMBER: _ClassVar[int]
    DEMOTE_FIELD_NUMBER: _ClassVar[int]
    Delete: GroupDelete
    Demote: _containers.RepeatedCompositeFieldContainer[JID]
    EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    Ephemeral: GroupEphemeral
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    JOINREASON_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    Join: _containers.RepeatedCompositeFieldContainer[JID]
    JoinReason: str
    LEAVE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    Leave: _containers.RepeatedCompositeFieldContainer[JID]
    Link: GroupLinkChange
    Locked: GroupLocked
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEWINVITELINK_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    Name: GroupName
    NewInviteLink: str
    Notify: str
    PARTICIPANTVERSIONID_FIELD_NUMBER: _ClassVar[int]
    PREVPARTICIPANTSVERSIONID_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_FIELD_NUMBER: _ClassVar[int]
    ParticipantVersionID: str
    PrevParticipantsVersionID: str
    Promote: _containers.RepeatedCompositeFieldContainer[JID]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    Sender: JID
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    Topic: GroupTopic
    UNKNOWNCHANGES_FIELD_NUMBER: _ClassVar[int]
    UNLINK_FIELD_NUMBER: _ClassVar[int]
    UnknownChanges: _containers.RepeatedCompositeFieldContainer[Node]
    Unlink: GroupLinkChange
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., Notify: _Optional[str] = ..., Sender: _Optional[_Union[JID, _Mapping]] = ..., Timestamp: _Optional[int] = ..., Name: _Optional[_Union[GroupName, _Mapping]] = ..., Topic: _Optional[_Union[GroupTopic, _Mapping]] = ..., Locked: _Optional[_Union[GroupLocked, _Mapping]] = ..., Announce: _Optional[_Union[GroupAnnounce, _Mapping]] = ..., Ephemeral: _Optional[_Union[GroupEphemeral, _Mapping]] = ..., Delete: _Optional[_Union[GroupDelete, _Mapping]] = ..., Link: _Optional[_Union[GroupLinkChange, _Mapping]] = ..., Unlink: _Optional[_Union[GroupLinkChange, _Mapping]] = ..., NewInviteLink: _Optional[str] = ..., PrevParticipantsVersionID: _Optional[str] = ..., ParticipantVersionID: _Optional[str] = ..., JoinReason: _Optional[str] = ..., Join: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., Leave: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., Promote: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., Demote: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., UnknownChanges: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class GroupIsDefaultSub(_message.Message):
    __slots__ = ["IsDefaultSubGroup"]
    ISDEFAULTSUBGROUP_FIELD_NUMBER: _ClassVar[int]
    IsDefaultSubGroup: bool
    def __init__(self, IsDefaultSubGroup: bool = ...) -> None: ...

class GroupLinkChange(_message.Message):
    __slots__ = ["Group", "Type", "UnlinkReason"]
    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    GROUP_FIELD_NUMBER: _ClassVar[int]
    Group: GroupLinkTarget
    PARENT: GroupLinkChange.ChangeType
    SIBLING: GroupLinkChange.ChangeType
    SUB: GroupLinkChange.ChangeType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: GroupLinkChange.ChangeType
    UNLINKREASON_FIELD_NUMBER: _ClassVar[int]
    UnlinkReason: str
    def __init__(self, Type: _Optional[_Union[GroupLinkChange.ChangeType, str]] = ..., UnlinkReason: _Optional[str] = ..., Group: _Optional[_Union[GroupLinkTarget, _Mapping]] = ...) -> None: ...

class GroupLinkTarget(_message.Message):
    __slots__ = ["GroupIsDefaultSub", "GroupName", "JID"]
    GROUPISDEFAULTSUB_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    GroupIsDefaultSub: GroupIsDefaultSub
    GroupName: GroupName
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., GroupName: _Optional[_Union[GroupName, _Mapping]] = ..., GroupIsDefaultSub: _Optional[_Union[GroupIsDefaultSub, _Mapping]] = ...) -> None: ...

class GroupLinkedParent(_message.Message):
    __slots__ = ["LinkedParentJID"]
    LINKEDPARENTJID_FIELD_NUMBER: _ClassVar[int]
    LinkedParentJID: JID
    def __init__(self, LinkedParentJID: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class GroupLocked(_message.Message):
    __slots__ = ["isLocked"]
    ISLOCKED_FIELD_NUMBER: _ClassVar[int]
    isLocked: bool
    def __init__(self, isLocked: bool = ...) -> None: ...

class GroupName(_message.Message):
    __slots__ = ["Name", "NameSetAt", "NameSetBy"]
    NAMESETAT_FIELD_NUMBER: _ClassVar[int]
    NAMESETBY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    NameSetAt: int
    NameSetBy: JID
    def __init__(self, Name: _Optional[str] = ..., NameSetAt: _Optional[int] = ..., NameSetBy: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class GroupParent(_message.Message):
    __slots__ = ["DefaultMembershipApprovalMode", "IsParent"]
    DEFAULTMEMBERSHIPAPPROVALMODE_FIELD_NUMBER: _ClassVar[int]
    DefaultMembershipApprovalMode: str
    ISPARENT_FIELD_NUMBER: _ClassVar[int]
    IsParent: bool
    def __init__(self, IsParent: bool = ..., DefaultMembershipApprovalMode: _Optional[str] = ...) -> None: ...

class GroupParticipant(_message.Message):
    __slots__ = ["AddRequest", "DisplayName", "Error", "IsAdmin", "IsSuperAdmin", "JID", "LID", "PhoneNumber"]
    ADDREQUEST_FIELD_NUMBER: _ClassVar[int]
    AddRequest: GroupParticipantAddRequest
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    DisplayName: str
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: int
    ISADMIN_FIELD_NUMBER: _ClassVar[int]
    ISSUPERADMIN_FIELD_NUMBER: _ClassVar[int]
    IsAdmin: bool
    IsSuperAdmin: bool
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    LID: JID
    LID_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    PhoneNumber: JID
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., LID: _Optional[_Union[JID, _Mapping]] = ..., PhoneNumber: _Optional[_Union[JID, _Mapping]] = ..., IsAdmin: bool = ..., IsSuperAdmin: bool = ..., DisplayName: _Optional[str] = ..., Error: _Optional[int] = ..., AddRequest: _Optional[_Union[GroupParticipantAddRequest, _Mapping]] = ...) -> None: ...

class GroupParticipantAddRequest(_message.Message):
    __slots__ = ["Code", "Expiration"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    Code: str
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    Expiration: float
    def __init__(self, Code: _Optional[str] = ..., Expiration: _Optional[float] = ...) -> None: ...

class GroupParticipantRequest(_message.Message):
    __slots__ = ["Participant", "TimeAt"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    Participant: JID
    TIMEAT_FIELD_NUMBER: _ClassVar[int]
    TimeAt: int
    def __init__(self, Participant: _Optional[_Union[JID, _Mapping]] = ..., TimeAt: _Optional[int] = ...) -> None: ...

class GroupTopic(_message.Message):
    __slots__ = ["Topic", "TopicDeleted", "TopicID", "TopicSetAt", "TopicSetBy"]
    TOPICDELETED_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    TOPICSETAT_FIELD_NUMBER: _ClassVar[int]
    TOPICSETBY_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    Topic: str
    TopicDeleted: bool
    TopicID: str
    TopicSetAt: int
    TopicSetBy: JID
    def __init__(self, Topic: _Optional[str] = ..., TopicID: _Optional[str] = ..., TopicSetAt: _Optional[int] = ..., TopicSetBy: _Optional[_Union[JID, _Mapping]] = ..., TopicDeleted: bool = ...) -> None: ...

class HistorySync(_message.Message):
    __slots__ = ["Data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    Data: _WAWebProtobufsHistorySync_pb2.HistorySync
    def __init__(self, Data: _Optional[_Union[_WAWebProtobufsHistorySync_pb2.HistorySync, _Mapping]] = ...) -> None: ...

class IdentityChange(_message.Message):
    __slots__ = ["Implicit", "JID", "Timestamp"]
    IMPLICIT_FIELD_NUMBER: _ClassVar[int]
    Implicit: bool
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., Timestamp: _Optional[int] = ..., Implicit: bool = ...) -> None: ...

class InfoQuery(_message.Message):
    __slots__ = ["Content", "Namespace", "To", "Type"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    Content: _containers.RepeatedCompositeFieldContainer[Node]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    Namespace: str
    TO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    To: str
    Type: str
    def __init__(self, Namespace: _Optional[str] = ..., Type: _Optional[str] = ..., To: _Optional[str] = ..., Content: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class IsOnWhatsAppResponse(_message.Message):
    __slots__ = ["IsIn", "JID", "Query", "VerifiedName"]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    IsIn: bool
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    Query: str
    VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
    VerifiedName: VerifiedName
    def __init__(self, Query: _Optional[str] = ..., JID: _Optional[_Union[JID, _Mapping]] = ..., IsIn: bool = ..., VerifiedName: _Optional[_Union[VerifiedName, _Mapping]] = ...) -> None: ...

class IsOnWhatsAppReturnFunction(_message.Message):
    __slots__ = ["Error", "IsOnWhatsAppResponse"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    ISONWHATSAPPRESPONSE_FIELD_NUMBER: _ClassVar[int]
    IsOnWhatsAppResponse: _containers.RepeatedCompositeFieldContainer[IsOnWhatsAppResponse]
    def __init__(self, IsOnWhatsAppResponse: _Optional[_Iterable[_Union[IsOnWhatsAppResponse, _Mapping]]] = ..., Error: _Optional[str] = ...) -> None: ...

class JID(_message.Message):
    __slots__ = ["Device", "Integrator", "IsEmpty", "RawAgent", "Server", "User"]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    Device: int
    INTEGRATOR_FIELD_NUMBER: _ClassVar[int]
    ISEMPTY_FIELD_NUMBER: _ClassVar[int]
    Integrator: int
    IsEmpty: bool
    RAWAGENT_FIELD_NUMBER: _ClassVar[int]
    RawAgent: int
    SERVER_FIELD_NUMBER: _ClassVar[int]
    Server: str
    USER_FIELD_NUMBER: _ClassVar[int]
    User: str
    def __init__(self, User: _Optional[str] = ..., RawAgent: _Optional[int] = ..., Device: _Optional[int] = ..., Integrator: _Optional[int] = ..., Server: _Optional[str] = ..., IsEmpty: bool = ...) -> None: ...

class JIDArray(_message.Message):
    __slots__ = ["JIDS"]
    JIDS: _containers.RepeatedCompositeFieldContainer[JID]
    JIDS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JIDS: _Optional[_Iterable[_Union[JID, _Mapping]]] = ...) -> None: ...

class JoinGroupWithLinkReturnFunction(_message.Message):
    __slots__ = ["Error", "Jid"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    JID_FIELD_NUMBER: _ClassVar[int]
    Jid: JID
    def __init__(self, Error: _Optional[str] = ..., Jid: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class JoinedGroup(_message.Message):
    __slots__ = ["CreateKey", "GroupInfo", "Reason", "Type"]
    CREATEKEY_FIELD_NUMBER: _ClassVar[int]
    CreateKey: str
    GROUPINFO_FIELD_NUMBER: _ClassVar[int]
    GroupInfo: GroupInfo
    REASON_FIELD_NUMBER: _ClassVar[int]
    Reason: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: str
    def __init__(self, Reason: _Optional[str] = ..., Type: _Optional[str] = ..., CreateKey: _Optional[str] = ..., GroupInfo: _Optional[_Union[GroupInfo, _Mapping]] = ...) -> None: ...

class KeepAliveRestored(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class KeepAliveTimeout(_message.Message):
    __slots__ = ["ErrorCount", "LastSuccess"]
    ERRORCOUNT_FIELD_NUMBER: _ClassVar[int]
    ErrorCount: int
    LASTSUCCESS_FIELD_NUMBER: _ClassVar[int]
    LastSuccess: int
    def __init__(self, ErrorCount: _Optional[int] = ..., LastSuccess: _Optional[int] = ...) -> None: ...

class LocalChatSettings(_message.Message):
    __slots__ = ["Archived", "Found", "MutedUntil", "Pinned"]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    Archived: bool
    FOUND_FIELD_NUMBER: _ClassVar[int]
    Found: bool
    MUTEDUNTIL_FIELD_NUMBER: _ClassVar[int]
    MutedUntil: float
    PINNED_FIELD_NUMBER: _ClassVar[int]
    Pinned: bool
    def __init__(self, Found: bool = ..., MutedUntil: _Optional[float] = ..., Pinned: bool = ..., Archived: bool = ...) -> None: ...

class LogEntry(_message.Message):
    __slots__ = ["Level", "Message", "Name"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    Level: str
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: str
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Message: _Optional[str] = ..., Level: _Optional[str] = ..., Name: _Optional[str] = ...) -> None: ...

class LoggedOut(_message.Message):
    __slots__ = ["OnConnect", "Reason"]
    ONCONNECT_FIELD_NUMBER: _ClassVar[int]
    OnConnect: bool
    REASON_FIELD_NUMBER: _ClassVar[int]
    Reason: ConnectFailureReason
    def __init__(self, OnConnect: bool = ..., Reason: _Optional[_Union[ConnectFailureReason, str]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["Info", "IsDocumentWithCaption", "IsEdit", "IsEphemeral", "IsLottieSticker", "IsViewOnce", "IsViewOnceV2", "IsViewOnceV2Extension", "Message", "NewsLetterMeta", "Raw", "RetryCount", "SourceWebMsg", "UnavailableRequestID"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ISDOCUMENTWITHCAPTION_FIELD_NUMBER: _ClassVar[int]
    ISEDIT_FIELD_NUMBER: _ClassVar[int]
    ISEPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    ISLOTTIESTICKER_FIELD_NUMBER: _ClassVar[int]
    ISVIEWONCEV2EXTENSION_FIELD_NUMBER: _ClassVar[int]
    ISVIEWONCEV2_FIELD_NUMBER: _ClassVar[int]
    ISVIEWONCE_FIELD_NUMBER: _ClassVar[int]
    Info: MessageInfo
    IsDocumentWithCaption: bool
    IsEdit: bool
    IsEphemeral: bool
    IsLottieSticker: bool
    IsViewOnce: bool
    IsViewOnceV2: bool
    IsViewOnceV2Extension: bool
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: _WAWebProtobufsE2E_pb2.Message
    NEWSLETTERMETA_FIELD_NUMBER: _ClassVar[int]
    NewsLetterMeta: NewsLetterMessageMeta
    RAW_FIELD_NUMBER: _ClassVar[int]
    RETRYCOUNT_FIELD_NUMBER: _ClassVar[int]
    Raw: _WAWebProtobufsE2E_pb2.Message
    RetryCount: int
    SOURCEWEBMSG_FIELD_NUMBER: _ClassVar[int]
    SourceWebMsg: _WAWebProtobufsWeb_pb2.WebMessageInfo
    UNAVAILABLEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    UnavailableRequestID: str
    def __init__(self, Info: _Optional[_Union[MessageInfo, _Mapping]] = ..., Message: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ..., IsEphemeral: bool = ..., IsViewOnce: bool = ..., IsViewOnceV2: bool = ..., IsViewOnceV2Extension: bool = ..., IsDocumentWithCaption: bool = ..., IsLottieSticker: bool = ..., IsEdit: bool = ..., SourceWebMsg: _Optional[_Union[_WAWebProtobufsWeb_pb2.WebMessageInfo, _Mapping]] = ..., UnavailableRequestID: _Optional[str] = ..., RetryCount: _Optional[int] = ..., NewsLetterMeta: _Optional[_Union[NewsLetterMessageMeta, _Mapping]] = ..., Raw: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageDebugTimings(_message.Message):
    __slots__ = ["GetDevices", "GetParticipants", "GroupEncrypt", "Marshal", "PeerEncrypt", "Queue", "Resp", "Retry", "Send"]
    GETDEVICES_FIELD_NUMBER: _ClassVar[int]
    GETPARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    GROUPENCRYPT_FIELD_NUMBER: _ClassVar[int]
    GetDevices: int
    GetParticipants: int
    GroupEncrypt: int
    MARSHAL_FIELD_NUMBER: _ClassVar[int]
    Marshal: int
    PEERENCRYPT_FIELD_NUMBER: _ClassVar[int]
    PeerEncrypt: int
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    Queue: int
    RESP_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    Resp: int
    Retry: int
    SEND_FIELD_NUMBER: _ClassVar[int]
    Send: int
    def __init__(self, Queue: _Optional[int] = ..., Marshal: _Optional[int] = ..., GetParticipants: _Optional[int] = ..., GetDevices: _Optional[int] = ..., GroupEncrypt: _Optional[int] = ..., PeerEncrypt: _Optional[int] = ..., Send: _Optional[int] = ..., Resp: _Optional[int] = ..., Retry: _Optional[int] = ...) -> None: ...

class MessageInfo(_message.Message):
    __slots__ = ["Category", "DeviceSentMeta", "Edit", "ID", "MediaType", "MessageSource", "Multicast", "Pushname", "ServerID", "Timestamp", "Type", "VerifiedName"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    Category: str
    DEVICESENTMETA_FIELD_NUMBER: _ClassVar[int]
    DeviceSentMeta: DeviceSentMeta
    EDIT_FIELD_NUMBER: _ClassVar[int]
    Edit: str
    ID: str
    ID_FIELD_NUMBER: _ClassVar[int]
    MEDIATYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGESOURCE_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_FIELD_NUMBER: _ClassVar[int]
    MediaType: str
    MessageSource: MessageSource
    Multicast: bool
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    Pushname: str
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    ServerID: int
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    Type: str
    VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
    VerifiedName: VerifiedName
    def __init__(self, MessageSource: _Optional[_Union[MessageSource, _Mapping]] = ..., ID: _Optional[str] = ..., ServerID: _Optional[int] = ..., Type: _Optional[str] = ..., Pushname: _Optional[str] = ..., Timestamp: _Optional[int] = ..., Category: _Optional[str] = ..., Multicast: bool = ..., MediaType: _Optional[str] = ..., Edit: _Optional[str] = ..., VerifiedName: _Optional[_Union[VerifiedName, _Mapping]] = ..., DeviceSentMeta: _Optional[_Union[DeviceSentMeta, _Mapping]] = ...) -> None: ...

class MessageSource(_message.Message):
    __slots__ = ["AddressingMode", "BroadcastListOwner", "BroadcastRecipients", "Chat", "IsFromMe", "IsGroup", "RecipientAlt", "Sender", "SenderAlt"]
    ADDRESSINGMODE_FIELD_NUMBER: _ClassVar[int]
    AddressingMode: AddressingMode
    BROADCASTLISTOWNER_FIELD_NUMBER: _ClassVar[int]
    BROADCASTRECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    BroadcastListOwner: JID
    BroadcastRecipients: _containers.RepeatedCompositeFieldContainer[BroadcastRecipient]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    Chat: JID
    ISFROMME_FIELD_NUMBER: _ClassVar[int]
    ISGROUP_FIELD_NUMBER: _ClassVar[int]
    IsFromMe: bool
    IsGroup: bool
    RECIPIENTALT_FIELD_NUMBER: _ClassVar[int]
    RecipientAlt: JID
    SENDERALT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    Sender: JID
    SenderAlt: JID
    def __init__(self, Chat: _Optional[_Union[JID, _Mapping]] = ..., Sender: _Optional[_Union[JID, _Mapping]] = ..., IsFromMe: bool = ..., IsGroup: bool = ..., AddressingMode: _Optional[_Union[AddressingMode, str]] = ..., SenderAlt: _Optional[_Union[JID, _Mapping]] = ..., RecipientAlt: _Optional[_Union[JID, _Mapping]] = ..., BroadcastListOwner: _Optional[_Union[JID, _Mapping]] = ..., BroadcastRecipients: _Optional[_Iterable[_Union[BroadcastRecipient, _Mapping]]] = ...) -> None: ...

class MutationInfo(_message.Message):
    __slots__ = ["Index", "Value", "Version"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    Index: _containers.RepeatedScalarFieldContainer[str]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    Value: _WASyncAction_pb2.SyncActionValue
    Version: int
    def __init__(self, Index: _Optional[_Iterable[str]] = ..., Version: _Optional[int] = ..., Value: _Optional[_Union[_WASyncAction_pb2.SyncActionValue, _Mapping]] = ...) -> None: ...

class NewsLetterMessageMeta(_message.Message):
    __slots__ = ["EditTS", "OriginalTS"]
    EDITTS_FIELD_NUMBER: _ClassVar[int]
    EditTS: int
    ORIGINALTS_FIELD_NUMBER: _ClassVar[int]
    OriginalTS: int
    def __init__(self, EditTS: _Optional[int] = ..., OriginalTS: _Optional[int] = ...) -> None: ...

class NewsletterJoin(_message.Message):
    __slots__ = ["NewsletterMetadata"]
    NEWSLETTERMETADATA_FIELD_NUMBER: _ClassVar[int]
    NewsletterMetadata: NewsletterMetadata
    def __init__(self, NewsletterMetadata: _Optional[_Union[NewsletterMetadata, _Mapping]] = ...) -> None: ...

class NewsletterLeave(_message.Message):
    __slots__ = ["ID", "Role"]
    ID: JID
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    Role: NewsletterRole
    def __init__(self, ID: _Optional[_Union[JID, _Mapping]] = ..., Role: _Optional[_Union[NewsletterRole, str]] = ...) -> None: ...

class NewsletterLiveUpdate(_message.Message):
    __slots__ = ["JID", "Messages", "TIME"]
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    Messages: _containers.RepeatedCompositeFieldContainer[NewsletterMessage]
    TIME: int
    TIME_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., TIME: _Optional[int] = ..., Messages: _Optional[_Iterable[_Union[NewsletterMessage, _Mapping]]] = ...) -> None: ...

class NewsletterMessage(_message.Message):
    __slots__ = ["Message", "MessageServerID", "ReactionCounts", "ViewsCount"]
    MESSAGESERVERID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: _WAWebProtobufsE2E_pb2.Message
    MessageServerID: int
    REACTIONCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ReactionCounts: _containers.RepeatedCompositeFieldContainer[Reaction]
    VIEWSCOUNT_FIELD_NUMBER: _ClassVar[int]
    ViewsCount: int
    def __init__(self, MessageServerID: _Optional[int] = ..., ViewsCount: _Optional[int] = ..., ReactionCounts: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ..., Message: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ...) -> None: ...

class NewsletterMetadata(_message.Message):
    __slots__ = ["ID", "State", "ThreadMeta", "ViewerMeta"]
    ID: JID
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    State: WrappedNewsletterState
    THREADMETA_FIELD_NUMBER: _ClassVar[int]
    ThreadMeta: NewsletterThreadMetadata
    VIEWERMETA_FIELD_NUMBER: _ClassVar[int]
    ViewerMeta: NewsletterViewerMetadata
    def __init__(self, ID: _Optional[_Union[JID, _Mapping]] = ..., State: _Optional[_Union[WrappedNewsletterState, _Mapping]] = ..., ThreadMeta: _Optional[_Union[NewsletterThreadMetadata, _Mapping]] = ..., ViewerMeta: _Optional[_Union[NewsletterViewerMetadata, _Mapping]] = ...) -> None: ...

class NewsletterMuteChange(_message.Message):
    __slots__ = ["ID", "Mute"]
    ID: JID
    ID_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    Mute: NewsletterMuteState
    def __init__(self, ID: _Optional[_Union[JID, _Mapping]] = ..., Mute: _Optional[_Union[NewsletterMuteState, str]] = ...) -> None: ...

class NewsletterReactionSettings(_message.Message):
    __slots__ = ["Value"]
    class NewsletterReactionsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: NewsletterReactionSettings.NewsletterReactionsMode
    BASIC: NewsletterReactionSettings.NewsletterReactionsMode
    BLOCKLIST: NewsletterReactionSettings.NewsletterReactionsMode
    NONE: NewsletterReactionSettings.NewsletterReactionsMode
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Value: NewsletterReactionSettings.NewsletterReactionsMode
    def __init__(self, Value: _Optional[_Union[NewsletterReactionSettings.NewsletterReactionsMode, str]] = ...) -> None: ...

class NewsletterSetting(_message.Message):
    __slots__ = ["ReactionCodes"]
    REACTIONCODES_FIELD_NUMBER: _ClassVar[int]
    ReactionCodes: NewsletterReactionSettings
    def __init__(self, ReactionCodes: _Optional[_Union[NewsletterReactionSettings, _Mapping]] = ...) -> None: ...

class NewsletterSubscribeLiveUpdatesReturnFunction(_message.Message):
    __slots__ = ["Duration", "Error"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    Duration: int
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, Duration: _Optional[int] = ..., Error: _Optional[str] = ...) -> None: ...

class NewsletterText(_message.Message):
    __slots__ = ["ID", "Text", "UpdateTime"]
    ID: str
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    Text: str
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UpdateTime: int
    def __init__(self, Text: _Optional[str] = ..., ID: _Optional[str] = ..., UpdateTime: _Optional[int] = ...) -> None: ...

class NewsletterThreadMetadata(_message.Message):
    __slots__ = ["CreationTime", "Description", "InviteCode", "Name", "Picture", "Preview", "Settings", "SubscriberCount", "VerificationState"]
    class NewsletterVerificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    CreationTime: int
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    Description: NewsletterText
    INVITECODE_FIELD_NUMBER: _ClassVar[int]
    InviteCode: str
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: NewsletterText
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    Picture: ProfilePictureInfo
    Preview: ProfilePictureInfo
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    Settings: NewsletterSetting
    SubscriberCount: int
    UNVERIFIED: NewsletterThreadMetadata.NewsletterVerificationState
    VERIFICATIONSTATE_FIELD_NUMBER: _ClassVar[int]
    VERIFIED: NewsletterThreadMetadata.NewsletterVerificationState
    VerificationState: NewsletterThreadMetadata.NewsletterVerificationState
    def __init__(self, CreationTime: _Optional[int] = ..., InviteCode: _Optional[str] = ..., Name: _Optional[_Union[NewsletterText, _Mapping]] = ..., Description: _Optional[_Union[NewsletterText, _Mapping]] = ..., SubscriberCount: _Optional[int] = ..., VerificationState: _Optional[_Union[NewsletterThreadMetadata.NewsletterVerificationState, str]] = ..., Picture: _Optional[_Union[ProfilePictureInfo, _Mapping]] = ..., Preview: _Optional[_Union[ProfilePictureInfo, _Mapping]] = ..., Settings: _Optional[_Union[NewsletterSetting, _Mapping]] = ...) -> None: ...

class NewsletterViewerMetadata(_message.Message):
    __slots__ = ["Mute", "Role"]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    Mute: NewsletterMuteState
    ROLE_FIELD_NUMBER: _ClassVar[int]
    Role: NewsletterRole
    def __init__(self, Mute: _Optional[_Union[NewsletterMuteState, str]] = ..., Role: _Optional[_Union[NewsletterRole, str]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ["Attrs", "Bytes", "Nil", "Nodes", "Tag"]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    Attrs: _containers.RepeatedCompositeFieldContainer[NodeAttrs]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    Bytes: bytes
    NIL_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    Nil: bool
    Nodes: _containers.RepeatedCompositeFieldContainer[Node]
    TAG_FIELD_NUMBER: _ClassVar[int]
    Tag: str
    def __init__(self, Tag: _Optional[str] = ..., Attrs: _Optional[_Iterable[_Union[NodeAttrs, _Mapping]]] = ..., Nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., Nil: bool = ..., Bytes: _Optional[bytes] = ...) -> None: ...

class NodeAttrs(_message.Message):
    __slots__ = ["boolean", "integer", "jid", "name", "text"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    JID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    integer: int
    jid: JID
    name: str
    text: str
    def __init__(self, name: _Optional[str] = ..., boolean: bool = ..., integer: _Optional[int] = ..., text: _Optional[str] = ..., jid: _Optional[_Union[JID, _Mapping]] = ...) -> None: ...

class OfflineSyncCompleted(_message.Message):
    __slots__ = ["Count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    Count: int
    def __init__(self, Count: _Optional[int] = ...) -> None: ...

class OfflineSyncPreview(_message.Message):
    __slots__ = ["AppDataChanges", "Message", "Notifications", "Receipts", "Total"]
    APPDATACHANGES_FIELD_NUMBER: _ClassVar[int]
    AppDataChanges: int
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: int
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    Notifications: int
    RECEIPTS_FIELD_NUMBER: _ClassVar[int]
    Receipts: int
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    Total: int
    def __init__(self, Total: _Optional[int] = ..., AppDataChanges: _Optional[int] = ..., Message: _Optional[int] = ..., Notifications: _Optional[int] = ..., Receipts: _Optional[int] = ...) -> None: ...

class PairPhoneParams(_message.Message):
    __slots__ = ["clientDisplayName", "clientType", "phone", "showPushNotification"]
    CLIENTDISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    CLIENTTYPE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    SHOWPUSHNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    clientDisplayName: str
    clientType: int
    phone: str
    showPushNotification: bool
    def __init__(self, phone: _Optional[str] = ..., showPushNotification: bool = ..., clientType: _Optional[int] = ..., clientDisplayName: _Optional[str] = ...) -> None: ...

class PairPhoneReturnFunction(_message.Message):
    __slots__ = ["Code", "Error"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    Code: str
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, Code: _Optional[str] = ..., Error: _Optional[str] = ...) -> None: ...

class PairStatus(_message.Message):
    __slots__ = ["BusinessName", "Error", "ID", "Platform", "Status"]
    class PStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BUSINESSNAME_FIELD_NUMBER: _ClassVar[int]
    BusinessName: str
    ERROR: PairStatus.PStatus
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    ID: JID
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    Platform: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS: PairStatus.PStatus
    Status: PairStatus.PStatus
    def __init__(self, ID: _Optional[_Union[JID, _Mapping]] = ..., BusinessName: _Optional[str] = ..., Platform: _Optional[str] = ..., Status: _Optional[_Union[PairStatus.PStatus, str]] = ..., Error: _Optional[str] = ...) -> None: ...

class PatchInfo(_message.Message):
    __slots__ = ["Mutations", "Timestamp", "Type"]
    class WAPatchName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CRITICAL_BLOCK: PatchInfo.WAPatchName
    CRITICAL_UNBLOCK_LOW: PatchInfo.WAPatchName
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    Mutations: _containers.RepeatedCompositeFieldContainer[MutationInfo]
    REGULAR: PatchInfo.WAPatchName
    REGULAR_HIGH: PatchInfo.WAPatchName
    REGULAR_LOW: PatchInfo.WAPatchName
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    Type: PatchInfo.WAPatchName
    def __init__(self, Timestamp: _Optional[int] = ..., Type: _Optional[_Union[PatchInfo.WAPatchName, str]] = ..., Mutations: _Optional[_Iterable[_Union[MutationInfo, _Mapping]]] = ...) -> None: ...

class Picture(_message.Message):
    __slots__ = ["Author", "JID", "Remove", "Timestamp"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    Author: JID
    JID: JID
    JID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    Remove: bool
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    def __init__(self, JID: _Optional[_Union[JID, _Mapping]] = ..., Author: _Optional[_Union[JID, _Mapping]] = ..., Timestamp: _Optional[int] = ..., Remove: bool = ...) -> None: ...

class Presence(_message.Message):
    __slots__ = ["From", "LastSeen", "Unavailable"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    From: JID
    LASTSEEN_FIELD_NUMBER: _ClassVar[int]
    LastSeen: int
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    Unavailable: bool
    def __init__(self, From: _Optional[_Union[JID, _Mapping]] = ..., Unavailable: bool = ..., LastSeen: _Optional[int] = ...) -> None: ...

class PrivacySettings(_message.Message):
    __slots__ = ["CallAdd", "GroupAdd", "LastSeen", "Online", "Profile", "ReadReceipts", "Status"]
    class PrivacySetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: PrivacySettings.PrivacySetting
    CALLADD_FIELD_NUMBER: _ClassVar[int]
    CONTACTS: PrivacySettings.PrivacySetting
    CONTACT_BLACKLIST: PrivacySettings.PrivacySetting
    CallAdd: PrivacySettings.PrivacySetting
    GROUPADD_FIELD_NUMBER: _ClassVar[int]
    GroupAdd: PrivacySettings.PrivacySetting
    KNOWN: PrivacySettings.PrivacySetting
    LASTSEEN_FIELD_NUMBER: _ClassVar[int]
    LastSeen: PrivacySettings.PrivacySetting
    MATCH_LAST_SEEN: PrivacySettings.PrivacySetting
    NONE: PrivacySettings.PrivacySetting
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    Online: PrivacySettings.PrivacySetting
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    Profile: PrivacySettings.PrivacySetting
    READRECEIPTS_FIELD_NUMBER: _ClassVar[int]
    ReadReceipts: PrivacySettings.PrivacySetting
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Status: PrivacySettings.PrivacySetting
    UNDEFINED: PrivacySettings.PrivacySetting
    def __init__(self, GroupAdd: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., LastSeen: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., Status: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., Profile: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., ReadReceipts: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., CallAdd: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ..., Online: _Optional[_Union[PrivacySettings.PrivacySetting, str]] = ...) -> None: ...

class ProfilePictureInfo(_message.Message):
    __slots__ = ["DirectPath", "Hash", "ID", "Type", "URL"]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    DirectPath: str
    HASH_FIELD_NUMBER: _ClassVar[int]
    Hash: bytes
    ID: str
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: str
    URL: str
    URL_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, URL: _Optional[str] = ..., ID: _Optional[str] = ..., Type: _Optional[str] = ..., DirectPath: _Optional[str] = ..., Hash: _Optional[bytes] = ...) -> None: ...

class QR(_message.Message):
    __slots__ = ["Codes"]
    CODES_FIELD_NUMBER: _ClassVar[int]
    Codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, Codes: _Optional[_Iterable[str]] = ...) -> None: ...

class Reaction(_message.Message):
    __slots__ = ["count", "type"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    count: int
    type: str
    def __init__(self, type: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class Receipt(_message.Message):
    __slots__ = ["MessageIDs", "MessageSource", "Timestamp", "Type"]
    class ReceiptType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DELIVERED: Receipt.ReceiptType
    HISTORY_SYNC: Receipt.ReceiptType
    INACTIVE: Receipt.ReceiptType
    MESSAGEIDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGESOURCE_FIELD_NUMBER: _ClassVar[int]
    MessageIDs: _containers.RepeatedScalarFieldContainer[str]
    MessageSource: MessageSource
    PEER_MSG: Receipt.ReceiptType
    PLAYED: Receipt.ReceiptType
    PLAYED_SELF: Receipt.ReceiptType
    READ: Receipt.ReceiptType
    READ_SELF: Receipt.ReceiptType
    RETRY: Receipt.ReceiptType
    SENDER: Receipt.ReceiptType
    SERVER_ERROR: Receipt.ReceiptType
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    Type: Receipt.ReceiptType
    def __init__(self, MessageSource: _Optional[_Union[MessageSource, _Mapping]] = ..., MessageIDs: _Optional[_Iterable[str]] = ..., Timestamp: _Optional[int] = ..., Type: _Optional[_Union[Receipt.ReceiptType, str]] = ...) -> None: ...

class ReqCreateGroup(_message.Message):
    __slots__ = ["CreateKey", "GroupLinkedParent", "GroupParent", "Participants", "name"]
    CREATEKEY_FIELD_NUMBER: _ClassVar[int]
    CreateKey: str
    GROUPLINKEDPARENT_FIELD_NUMBER: _ClassVar[int]
    GROUPPARENT_FIELD_NUMBER: _ClassVar[int]
    GroupLinkedParent: GroupLinkedParent
    GroupParent: GroupParent
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    Participants: _containers.RepeatedCompositeFieldContainer[JID]
    name: str
    def __init__(self, name: _Optional[str] = ..., Participants: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., CreateKey: _Optional[str] = ..., GroupParent: _Optional[_Union[GroupParent, _Mapping]] = ..., GroupLinkedParent: _Optional[_Union[GroupLinkedParent, _Mapping]] = ...) -> None: ...

class ResolveBusinessMessageLinkReturnFunction(_message.Message):
    __slots__ = ["Error", "MessageLinkTarget"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    MESSAGELINKTARGET_FIELD_NUMBER: _ClassVar[int]
    MessageLinkTarget: BusinessMessageLinkTarget
    def __init__(self, MessageLinkTarget: _Optional[_Union[BusinessMessageLinkTarget, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class ResolveContactQRLinkReturnFunction(_message.Message):
    __slots__ = ["ContactQrLink", "Error"]
    CONTACTQRLINK_FIELD_NUMBER: _ClassVar[int]
    ContactQrLink: ContactQRLinkTarget
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    def __init__(self, ContactQrLink: _Optional[_Union[ContactQRLinkTarget, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class ReturnFunctionWithError(_message.Message):
    __slots__ = ["Error", "GetLinkedGroupsParticipants", "LocalChatSettings", "PollVoteMessage"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    GETLINKEDGROUPSPARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    GetLinkedGroupsParticipants: JIDArray
    LOCALCHATSETTINGS_FIELD_NUMBER: _ClassVar[int]
    LocalChatSettings: LocalChatSettings
    POLLVOTEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PollVoteMessage: _WAWebProtobufsE2E_pb2.PollVoteMessage
    def __init__(self, Error: _Optional[str] = ..., LocalChatSettings: _Optional[_Union[LocalChatSettings, _Mapping]] = ..., PollVoteMessage: _Optional[_Union[_WAWebProtobufsE2E_pb2.PollVoteMessage, _Mapping]] = ..., GetLinkedGroupsParticipants: _Optional[_Union[JIDArray, _Mapping]] = ...) -> None: ...

class SendMessageReturnFunction(_message.Message):
    __slots__ = ["Error", "SendResponse"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    SENDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SendResponse: SendResponse
    def __init__(self, Error: _Optional[str] = ..., SendResponse: _Optional[_Union[SendResponse, _Mapping]] = ...) -> None: ...

class SendRequestExtra(_message.Message):
    __slots__ = ["ID", "InlineBotJID", "MediaHandle", "Peer", "Timeout"]
    ID: str
    ID_FIELD_NUMBER: _ClassVar[int]
    INLINEBOTJID_FIELD_NUMBER: _ClassVar[int]
    InlineBotJID: JID
    MEDIAHANDLE_FIELD_NUMBER: _ClassVar[int]
    MediaHandle: str
    PEER_FIELD_NUMBER: _ClassVar[int]
    Peer: bool
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    Timeout: int
    def __init__(self, ID: _Optional[str] = ..., InlineBotJID: _Optional[_Union[JID, _Mapping]] = ..., Peer: bool = ..., Timeout: _Optional[int] = ..., MediaHandle: _Optional[str] = ...) -> None: ...

class SendResponse(_message.Message):
    __slots__ = ["DebugTimings", "ID", "Message", "ServerID", "Timestamp"]
    DEBUGTIMINGS_FIELD_NUMBER: _ClassVar[int]
    DebugTimings: MessageDebugTimings
    ID: str
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: _WAWebProtobufsE2E_pb2.Message
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    ServerID: int
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    Timestamp: int
    def __init__(self, Timestamp: _Optional[int] = ..., ID: _Optional[str] = ..., ServerID: _Optional[int] = ..., DebugTimings: _Optional[_Union[MessageDebugTimings, _Mapping]] = ..., Message: _Optional[_Union[_WAWebProtobufsE2E_pb2.Message, _Mapping]] = ...) -> None: ...

class SetGroupPhotoReturnFunction(_message.Message):
    __slots__ = ["Error", "PictureID"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    PICTUREID_FIELD_NUMBER: _ClassVar[int]
    PictureID: str
    def __init__(self, PictureID: _Optional[str] = ..., Error: _Optional[str] = ...) -> None: ...

class SetPrivacySettingReturnFunction(_message.Message):
    __slots__ = ["Error", "settings"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PrivacySettings
    def __init__(self, settings: _Optional[_Union[PrivacySettings, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class StatusPrivacy(_message.Message):
    __slots__ = ["IsDefault", "List", "Type"]
    class StatusPrivacyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLACKLIST: StatusPrivacy.StatusPrivacyType
    CONTACTS: StatusPrivacy.StatusPrivacyType
    ISDEFAULT_FIELD_NUMBER: _ClassVar[int]
    IsDefault: bool
    LIST_FIELD_NUMBER: _ClassVar[int]
    List: _containers.RepeatedCompositeFieldContainer[JID]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: StatusPrivacy.StatusPrivacyType
    WHITELIST: StatusPrivacy.StatusPrivacyType
    def __init__(self, Type: _Optional[_Union[StatusPrivacy.StatusPrivacyType, str]] = ..., List: _Optional[_Iterable[_Union[JID, _Mapping]]] = ..., IsDefault: bool = ...) -> None: ...

class Stop(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StreamError(_message.Message):
    __slots__ = ["Code", "Raw"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    Code: str
    RAW_FIELD_NUMBER: _ClassVar[int]
    Raw: Node
    def __init__(self, Code: _Optional[str] = ..., Raw: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class StreamReplaced(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TemporaryBan(_message.Message):
    __slots__ = ["Code", "Expire"]
    class TempBanReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLOCKED_BY_USERS: TemporaryBan.TempBanReason
    BROADCAST_LIST: TemporaryBan.TempBanReason
    CODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TOO_MANY_GROUPS: TemporaryBan.TempBanReason
    Code: TemporaryBan.TempBanReason
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    Expire: int
    SEND_TO_TOO_MANY_PEOPLE: TemporaryBan.TempBanReason
    SENT_TOO_MANY_SAME_MESSAGE: TemporaryBan.TempBanReason
    def __init__(self, Code: _Optional[_Union[TemporaryBan.TempBanReason, str]] = ..., Expire: _Optional[int] = ...) -> None: ...

class UndecryptableMessage(_message.Message):
    __slots__ = ["DecryptFailMode", "Info", "IsUnavailable"]
    class DecryptFailModeT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DECRYPTFAILMODE_FIELD_NUMBER: _ClassVar[int]
    DECRYPT_FAIL_HIDE: UndecryptableMessage.DecryptFailModeT
    DECRYPT_FAIL_SHOW: UndecryptableMessage.DecryptFailModeT
    DecryptFailMode: UndecryptableMessage.DecryptFailModeT
    INFO_FIELD_NUMBER: _ClassVar[int]
    ISUNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    Info: MessageInfo
    IsUnavailable: bool
    def __init__(self, Info: _Optional[_Union[MessageInfo, _Mapping]] = ..., IsUnavailable: bool = ..., DecryptFailMode: _Optional[_Union[UndecryptableMessage.DecryptFailModeT, str]] = ...) -> None: ...

class UnknownCallEvent(_message.Message):
    __slots__ = ["node"]
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: Node
    def __init__(self, node: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class UpdateGroupParticipantsReturnFunction(_message.Message):
    __slots__ = ["Error", "participants"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[GroupParticipant]
    def __init__(self, Error: _Optional[str] = ..., participants: _Optional[_Iterable[_Union[GroupParticipant, _Mapping]]] = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = ["DirectPath", "FileEncSHA256", "FileLength", "FileSHA256", "Handle", "MediaKey", "url"]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    DirectPath: str
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FileEncSHA256: bytes
    FileLength: int
    FileSHA256: bytes
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    Handle: str
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    MediaKey: bytes
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ..., DirectPath: _Optional[str] = ..., Handle: _Optional[str] = ..., MediaKey: _Optional[bytes] = ..., FileEncSHA256: _Optional[bytes] = ..., FileSHA256: _Optional[bytes] = ..., FileLength: _Optional[int] = ...) -> None: ...

class UploadReturnFunction(_message.Message):
    __slots__ = ["Error", "UploadResponse"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Error: str
    UPLOADRESPONSE_FIELD_NUMBER: _ClassVar[int]
    UploadResponse: UploadResponse
    def __init__(self, UploadResponse: _Optional[_Union[UploadResponse, _Mapping]] = ..., Error: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["Devices", "PictureID", "Status", "VerifiedName"]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    Devices: _containers.RepeatedCompositeFieldContainer[JID]
    PICTUREID_FIELD_NUMBER: _ClassVar[int]
    PictureID: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Status: str
    VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
    VerifiedName: VerifiedName
    def __init__(self, VerifiedName: _Optional[_Union[VerifiedName, _Mapping]] = ..., Status: _Optional[str] = ..., PictureID: _Optional[str] = ..., Devices: _Optional[_Iterable[_Union[JID, _Mapping]]] = ...) -> None: ...

class VerifiedName(_message.Message):
    __slots__ = ["Certificate", "Details"]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    Certificate: _WAWebProtobufsVnameCert_pb2.VerifiedNameCertificate
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    Details: _WAWebProtobufsVnameCert_pb2.VerifiedNameCertificate.Details
    def __init__(self, Certificate: _Optional[_Union[_WAWebProtobufsVnameCert_pb2.VerifiedNameCertificate, _Mapping]] = ..., Details: _Optional[_Union[_WAWebProtobufsVnameCert_pb2.VerifiedNameCertificate.Details, _Mapping]] = ...) -> None: ...

class WrappedNewsletterState(_message.Message):
    __slots__ = ["Type"]
    class NewsletterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: WrappedNewsletterState.NewsletterState
    GEOSUSPENDED: WrappedNewsletterState.NewsletterState
    SUSPENDED: WrappedNewsletterState.NewsletterState
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: WrappedNewsletterState.NewsletterState
    def __init__(self, Type: _Optional[_Union[WrappedNewsletterState.NewsletterState, str]] = ...) -> None: ...

class privacySettingsEvent(_message.Message):
    __slots__ = ["CallAddChanged", "GroupAddChanged", "LastSeenChanged", "NewSettings", "OnlineChanged", "ProfileChanged", "ReadReceiptsChanged", "StatusChanged"]
    CALLADDCHANGED_FIELD_NUMBER: _ClassVar[int]
    CallAddChanged: bool
    GROUPADDCHANGED_FIELD_NUMBER: _ClassVar[int]
    GroupAddChanged: bool
    LASTSEENCHANGED_FIELD_NUMBER: _ClassVar[int]
    LastSeenChanged: bool
    NEWSETTINGS_FIELD_NUMBER: _ClassVar[int]
    NewSettings: PrivacySettings
    ONLINECHANGED_FIELD_NUMBER: _ClassVar[int]
    OnlineChanged: bool
    PROFILECHANGED_FIELD_NUMBER: _ClassVar[int]
    ProfileChanged: bool
    READRECEIPTSCHANGED_FIELD_NUMBER: _ClassVar[int]
    ReadReceiptsChanged: bool
    STATUSCHANGED_FIELD_NUMBER: _ClassVar[int]
    StatusChanged: bool
    def __init__(self, NewSettings: _Optional[_Union[PrivacySettings, _Mapping]] = ..., GroupAddChanged: bool = ..., LastSeenChanged: bool = ..., StatusChanged: bool = ..., ProfileChanged: bool = ..., ReadReceiptsChanged: bool = ..., OnlineChanged: bool = ..., CallAddChanged: bool = ...) -> None: ...

class AddressingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NewsletterRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NewsletterMuteState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConnectFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
