"""
Dwarf - Copyright (C) 2019 Giovanni Rocca (iGio90)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import frida

from lib.session.session import Session


class LocalSession(Session):

    def __init__(self, app_window):
        super(LocalSession, self).__init__(app_window)

    @property
    def session_ui_sections(self):
        # what sections we want in session_ui
        return ['hooks', 'bookmarks', 'threads', 'registers', 'debug', 'console', 'watchers', 'backtrace']

    @property
    def non_closable(self):
        return ['debug', 'ranges', 'modules']

    @property
    def session_type(self):
        """ return session name to show in menus etc
        """
        return 'local'

    @property
    def device_manager_type(self):
        return 'local'

    @property
    def frida_device(self):
        return frida.get_local_device()
