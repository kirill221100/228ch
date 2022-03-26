from flask_admin import AdminIndexView, expose
from app import basic_auth



class DashboardView(AdminIndexView):
    @expose('/')
    @basic_auth.required
    def index(self):
        return self.render('admin/dashboard_index.html')
