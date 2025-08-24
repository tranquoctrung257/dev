import os
# dep link mở profile bằng id
"""

adb shell am start -d "snssdk1233://user/profile/123456" -n com.ss.android.ugc.trill/com.ss.android.ugc.aweme.deeplink.DeepLinkActivityV2

"""

# snssdk1128://
os.system('adb shell am start -d "snssdk1128://goods/seeding/?promotion_id=4534" -n com.ss.android.ugc.trill/com.ss.android.ugc.aweme.deeplink.DeepLinkActivityV2')