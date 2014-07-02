# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.tmpl_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from web import my_form
from tekton import router

@login_not_required
@no_csrf
def index():
    return TemplateResponse({'form_url': router.to_path(my_form)})
