import Admin.service
Admin.service.admin_service()


import Admin.product
Admin.product.admin_product()



import Admin.Common.header
Admin.Common.header.admin_common_header()



import Tech.profile
Tech.profile.tech_profile()


from Admin import service
service.admin_service()


from Admin.Common import header
header.admin_common_header()



from User import profile
profile.user_profile()


from User import request
request.user_request()

from Admin import *
service.admin_service()
product.admin_product()

from Admin import *
from Admin.Common import *
header.admin_common_header()
footer.admin_common_footer()
service.admin_service()
product.admin_product()


from Tech import work
work.tech_work()
