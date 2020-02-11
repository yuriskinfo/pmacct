#
#   pmacct (Promiscuous mode IP Accounting package)
#   pmacct is Copyright (C) 2003-2020 by Paolo Lucente
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#   pmgrpcd and its components are Copyright (C) 2018-2020 by:
#
#   Matthias Arnold <matthias.arnold@swisscom.com>
#   Juan Camilo Cardona <jccardona82@gmail.com>
#   Thomas Graf <thomas.graf@swisscom.com>
#   Paolo Lucente <paolo@pmacct.net>
#
from export_pmgrpcd import Exporter
import os
import ujson as json

class FileExporter(Exporter):
    def __init__(self, output_file):
        self.output_file = output_file

    def process_metric(self, datajsonstring):
        jsondata = json.loads(datajsonstring)
        again_json = json.dumps(jsondata).replace("\n", "")
        # we'll probably remove the loading here
        with open(self.output_file, 'a') as fh:
            fh.write(again_json)
            fh.write("\n")

