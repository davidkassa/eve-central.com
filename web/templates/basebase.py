#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from templates.pythonbase import pythonbase
from mx.DateTime import gmt
import random

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1346110082.078216
__CHEETAH_genTimestamp__ = 'Mon Aug 27 23:28:02 2012'
__CHEETAH_src__ = 'basebase.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Aug 27 23:24:02 2012'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class basebase(pythonbase):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(basebase, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def title(self, **KWS):



        ## CHEETAH: generated from #def title at line 9, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''Untitled
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def banner(self, **KWS):



        ## CHEETAH: generated from #def banner at line 13, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFFSL(SL,"title",True) # u'$title' on line 14, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 14, col 1.
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 17, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<div id="bodyText">
No body! :)
</div>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def _title(self, **KWS):



        ## CHEETAH: generated from #block _title at line 58, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''
''')
        if VFN(VFFSL(SL,"title",True),"find",False)("EVE-Central") != -1: # generated from line 60, col 1
            pass
        else: # generated from line 62, col 1
            write(u''' EVE-Central -
''')
        write(u''' ''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 65, col 2
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 65, col 2.
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def _banner(self, **KWS):



        ## CHEETAH: generated from #block _banner at line 98, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<h1>''')
        _v = VFFSL(SL,"banner",True) # u'$banner' on line 99, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$banner')) # from line 99, col 5.
        write(u'''</h1>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''





<!DOCTYPE html>
<html>
<!--
#    EVE-Central.com Codebase
#    Copyright (C) 2006-2012 StackFoundry LLC and Yann Ramin
''')
        write(u'''#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
''')
        write(u'''#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
''')
        write(u'''#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->

<head>
<link href="/css/normalize.css" rel="stylesheet" type="text/css" />
<link href="/css/style.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css" href="/js/yui/autocomplete/assets/skins/sam/autocomplete.css" />

<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-84549-2";
urchinTracker();
</script>

<script type="text/javascript" src="/js/jquery.min.js"></script>
<script type="text/javascript" src="/js/evec.js"></script>
  <title>
''')
        self._title(trans=trans)
        write(u'''</title>

</head>

<body>


''')
        timehead = gmt()
        write(u'''


<div class="topbar">
  <ul>
    <li><a href="/"><img src="/images/evec_logo.png"></a></li>
    <li><a href="/home/market.html">Market</a></li>
    <li><a href="/tradetool/">Trade Tools</a></li>
    <li><a href="/home/develop.html">API</a></li>
    <li><a href="/home/software.html">Contribute</a></li>
    <li class="right">
''')
        _v = VFN(VFFSL(SL,"timehead",True),"Format",False)("%b %e %H:%M") # u'$timehead.Format("%b %e %H:%M")' on line 86, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$timehead.Format("%b %e %H:%M")')) # from line 86, col 1.
        write(u''' 
GMT
    </li>

    <li class="right"><form method="get" action="/home/typesearch.html">
<input type="text" name="search" placeholder="Item name"> <button type="submit" value="Search">Search</button>
</form>
    </li>
  </ul>
</div>


''')
        self._banner(trans=trans)
        write(u'''
<div id="bodyText">
''')
        _v = VFFSL(SL,"body",True) # u'$body' on line 103, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$body')) # from line 103, col 1.
        write(u'''
</div>
    

    
    
    <div id="footer">

<p class="adLink">
<b>EVETIMECODE buy 14 etc get 1 free <a href="http://evetimecode.com">EVETIMECODE.com</a> - Where your business counts!</b>
</p>

<p class="adLink">
<b><a href="http://www.shatteredcrystal.com/code.php/eve_online/~325">EVE Online Game Time Codes</a></b> - Support EVE-Central by purchasing them at ShatteredCrystal.com through this affiliate link.</p>
<p>

<table border=0>
<tr>
<td>
<script type="text/javascript"><!--
google_ad_client = "ca-pub-8691225504311148";
/* Big Banner */
google_ad_slot = "8769907779";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</td>
<td>
<!-- Project Wonderful Ad Box Loader -->
<!-- Put this after the <body> tag at the top of your page -->
<script type="text/javascript">
   (function(){function pw_load(){
      if(arguments.callee.z)return;else arguments.callee.z=true;
      var d=document;var s=d.createElement(\'script\');
      var x=d.getElementsByTagName(\'script\')[0];
      s.type=\'text/javascript\';s.async=true;
      s.src=\'//www.projectwonderful.com/pwa.js\';
      x.parentNode.insertBefore(s,x);}
   if (window.attachEvent){
    window.attachEvent(\'DOMContentLoaded\',pw_load);
    window.attachEvent(\'onload\',pw_load);}
   else{
    window.addEventListener(\'DOMContentLoaded\',pw_load,false);
    window.addEventListener(\'load\',pw_load,false);}})();
</script>
<!-- End Project Wonderful Ad Box Loader -->
<!-- Project Wonderful Ad Box Code -->
<div id="pw_adbox_61086_2_0"></div>
<!-- End Project Wonderful Ad Box Code -->

</td></tr></table>


<br />
&copy; 2005-2012 <a href="http://www.stackworks.net/">StackFoundry LLC</a>    Feedback? Bug reports? Send them to Yann at <a href="mailto:yann [at] stackfoundry.com">yann [at] stackfoundry.com</a>.  EVE-Central.com uses advertising and affiliate links to help offset the cost of co-location, servers and bandwidth. The EVE-Central.com code base is <a href="http://dev.eve-central.com/eve-central/">made available</a> under the <a href="http://www.fsf.org/licensing/licenses/agpl-3.0.html">Affero GPL (AGPL) version 3.0 or later. </a> Material related to EVE-Online is used with limited permission of CCP Games hf. No official affiliation or endorsement by CCP Games hf is stated or implied.



</div>
</body>
</html>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_basebase= u'respond'

## END CLASS DEFINITION

if not hasattr(basebase, '_initCheetahAttributes'):
    templateAPIClass = getattr(basebase, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(basebase)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=basebase()).run()


