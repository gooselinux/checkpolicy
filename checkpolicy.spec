%define libsepolver 2.0.39-1
Summary: SELinux policy compiler
Name: checkpolicy
Version: 2.0.22
Release: 1%{?dist}
License: GPLv2
Group: Development/System
Source: http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
Patch: checkpolicy-rhat.patch

BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: byacc bison flex libsepol-static >= %{libsepolver} libselinux-devel

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.  
Only required for building policies. 

%prep
%setup -q
%patch -p1 -b .rhat

%build
make clean
make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 
cd test
make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
make LIBDIR="%{_libdir}" DESTDIR="${RPM_BUILD_ROOT}" install
install test/dismod ${RPM_BUILD_ROOT}%{_bindir}/sedismod
install test/dispol ${RPM_BUILD_ROOT}%{_bindir}/sedispol

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8.gz
%{_mandir}/man8/checkmodule.8.gz
%{_bindir}/sedismod
%{_bindir}/sedispol

%changelog
* Mon Jun 16 2010 Dan Walsh <dwalsh@redhat.com> - 2.0.22-1
- Latest update from NSA
	* Update checkmodule man page and usage by Daniel Walsh and Steve Lawrence
- Allow policy version to be one number
Resolves: #588260

* Mon May 3 2010 Dan Walsh <dwalsh@redhat.com> - 2.0.21-2
- Fix checkmodule man page and usage statements

* Tue Nov 1 2009 Dan Walsh <dwalsh@redhat.com> - 2.0.21-1
- Latest update from NSA
	* Add support for building Xen policies from Paul Nuzzi.
	* Add long options to checkpolicy and checkmodule by Guido
	  Trentalancia <guido@trentalancia.com>

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Dan Walsh <dwalsh@redhat.com> - 2.0.19-1
- Latest update from NSA
	* Fix alias field in module format, caused by boundary format change
	  from Caleb Case.

* Fri Jan 30 2009 Dan Walsh <dwalsh@redhat.com> - 2.0.18-1
- Latest update from NSA
	* Properly escape regex symbols in the lexer from Stephen Smalley.
	* Add bounds support from KaiGai Kohei.

* Tue Oct 28 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.16-4

* Mon Jul 7 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.16-3
- Rebuild with new libsepol

* Wed May 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.16-2
- fix license tag

* Wed May 28 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.16-1
- Latest update from NSA
	* Update checkpolicy for user and role mapping support from Joshua Brindle.

* Tue May 2 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.15-1
- Latest update from NSA
	* Fix for policy module versions that look like IPv4 addresses from Jim Carter.
	  Resolves bug 444451.

* Tue May 2 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.14-2
- Allow modules with 4 sections or more

* Thu Mar 27 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.14-1
- Latest update from NSA
	* Add permissive domain support from Eric Paris.

* Thu Mar 13 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.13-1
- Latest update from NSA
	* Split out non-grammar parts of policy_parse.yacc into
	  policy_define.c and policy_define.h from Todd C. Miller.
	* Initialize struct policy_file before using it, from Todd C. Miller.
	* Remove unused define, move variable out of .y file, simplify COND_ERR, from Todd C. Miller.

* Thu Feb 28 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.10-1
- Latest update from NSA
	* Use yyerror2() where appropriate from Todd C. Miller.
- Build against latest libsepol

* Fri Feb 22 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.9-2
- Start shipping sedismod and sedispol

* Mon Feb 4 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.9-1
- Latest update from NSA
	* Update dispol for libsepol avtab changes from Stephen Smalley.

* Fri Jan 25 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.8-1
- Latest update from NSA
	* Deprecate role dominance in parser.

* Mon Jan 21 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.7-2
- Update to use libsepol-static library

* Fri Jan 11 2008 Dan Walsh <dwalsh@redhat.com> - 2.0.7-1
- Latest update from NSA
	* Added support for policy capabilities from Todd Miller.

* Thu Nov 15 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.6-1
- Latest update from NSA
	* Initialize the source file name from the command line argument so that checkpolicy/checkmodule report something more useful than "unknown source".
	* Merged remove use of REJECT and trailing context in lex rules; make ipv4 address parsing like ipv6 from James Carter.

* Tue Sep 18 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.4-1
	* Merged handle unknown policydb flag support from Eric Paris.
	  Adds new command line options -U {allow, reject, deny} for selecting
	  the flag when a base module or kernel policy is built.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.0.3-3
- Rebuild for selinux ppc32 issue.

* Thu Jun 18 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.3-2
- Rebuild with the latest libsepol

* Thu Jun 17 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.3-1
- Latest update from NSA
	* Merged fix for segfault on duplicate require of sensitivity from Caleb Case.
	* Merged fix for dead URLs in checkpolicy man pages from Dan Walsh.

* Thu Apr 12 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.2-1
- Latest update from NSA
	* Merged checkmodule man page fix from Dan Walsh.

* Fri Mar 30 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.1-3
- Rebuild with new libsepol

* Wed Mar 28 2007 Dan Walsh <dwalsh@redhat.com> - 2.0.1-2
- Rebuild with new libsepol

* Tue Nov 20 2006 Dan Walsh <dwalsh@redhat.com> - 2.0.1-1
- Latest update from NSA
	* Merged patch to allow dots in class identifiers from Caleb Case.

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> - 2.0.0-1
- Latest update from NSA
	* Merged patch to use new libsepol error codes by Karl MacMillan.
	* Updated version for stable branch.

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> - 1.33.1-2
- Rebuild for new libraries

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> - 1.33.1-1
- Latest update from NSA
	* Collapse user identifiers and identifiers together.

* Tue Oct 17 2006 Dan Walsh <dwalsh@redhat.com> - 1.32-1
- Latest update from NSA
	* Updated version for release.

* Thu Sep 28 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.12-1
- Latest update from NSA
	* Merged user and range_transition support for modules from 
	  Darrel Goeddel

* Wed Sep 6 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.11-1
- Latest update from NSA
	* merged range_transition enhancements and user module format
	  changes from Darrel Goeddel
	* Merged symtab datum patch from Karl MacMillan.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.30.9-1.1
- rebuild

* Tue Jul 4 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.8-1
- Latest upgrade from NSA
	* Lindent.
	* Merged patch to remove TE rule conflict checking from the parser
	  from Joshua Brindle.  This can only be done properly by the 
	  expander.
	* Merged patch to make checkpolicy/checkmodule handling of
	  duplicate/conflicting TE rules the same as the expander 
	  from Joshua Brindle.
	* Merged optionals in base take 2 patch set from Joshua Brindle.

* Wed May 23 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.5-1
- Latest upgrade from NSA
	* Merged compiler cleanup patch from Karl MacMillan.
	* Merged fix warnings patch from Karl MacMillan.	

* Wed Apr 5 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.4-1
- Latest upgrade from NSA
	* Changed require_class to reject permissions that have not been
	  declared if building a base module.

* Tue Mar 28 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.3-1
- Latest upgrade from NSA
	* Fixed checkmodule to call link_modules prior to expand_module
	  to handle optionals.
	* Fixed require_class to avoid shadowing permissions already defined
	  in an inherited common definition.

* Mon Mar 27 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.1-2
- Rebuild with new libsepol

* Thu Mar 23 2006 Dan Walsh <dwalsh@redhat.com> - 1.30.1-1
- Latest upgrade from NSA
	* Moved processing of role and user require statements to 2nd pass.

* Fri Mar 17 2006 Dan Walsh <dwalsh@redhat.com> - 1.30-1
- Latest upgrade from NSA
	* Updated version for release.
	* Fixed bug in role dominance (define_role_dom).

* Fri Feb 17 2006 Dan Walsh <dwalsh@redhat.com> - 1.29.4-1
- Latest upgrade from NSA
	* Added a check for failure to declare each sensitivity in
	  a level definition.
	* Changed to clone level data for aliased sensitivities to
	  avoid double free upon sens_destroy.  Bug reported by Kevin
	  Carr of Tresys Technology.

* Mon Feb 13 2006 Dan Walsh <dwalsh@redhat.com> - 1.29.2-1
- Latest upgrade from NSA
	* Merged optionals in base patch from Joshua Brindle.

* Mon Feb 13 2006 Dan Walsh <dwalsh@redhat.com> - 1.29.1-1.2
- Need to build againi

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.29.1-1.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Dan Walsh <dwalsh@redhat.com> 1.29.1-1
- Latest upgrade from NSA
	* Merged sepol_av_to_string patch from Joshua Brindle.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.28-5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Dan Walsh <dwalsh@redhat.com> 1.28-5
- Rebuild to get latest libsepol

* Fri Jan 13 2006 Dan Walsh <dwalsh@redhat.com> 1.28-5
- Rebuild to get latest libsepol

* Thu Jan 5 2006 Dan Walsh <dwalsh@redhat.com> 1.28-4
- Rebuild to get latest libsepol

* Wed Jan 4 2006 Dan Walsh <dwalsh@redhat.com> 1.28-3
- Rebuild to get latest libsepol

* Fri Dec 16 2005 Dan Walsh <dwalsh@redhat.com> 1.28-2
- Rebuild to get latest libsepol

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec 9 2005 Dan Walsh <dwalsh@redhat.com> 1.28-1
- Latest upgrade from NSA

* Sun Dec 4 2005 Dan Walsh <dwalsh@redhat.com> 1.27.20-1
- Latest upgrade from NSA
	* Merged checkmodule man page from Dan Walsh, and edited it.

* Thu Dec 1 2005 Dan Walsh <dwalsh@redhat.com> 1.27.19-1
- Latest upgrade from NSA
	* Added error checking of all ebitmap_set_bit calls for out of
	  memory conditions.
	* Merged removal of compatibility handling of netlink classes
	  (requirement that policies with newer versions include the
	   netlink class definitions, remapping of fine-grained netlink
	   classes in newer source policies to single netlink class when
	   generating older policies) from George Coker.

* Tue Nov 8 2005 Dan Walsh <dwalsh@redhat.com> 1.27.17-7
- Rebuild to get latest libsepol

* Tue Oct 25 2005 Dan Walsh <dwalsh@redhat.com> 1.27.17-1
- Latest upgrade from NSA
	* Merged dismod fix from Joshua Brindle.

* Thu Oct 20 2005 Dan Walsh <dwalsh@redhat.com> 1.27.16-1
- Latest upgrade from NSA
	* Removed obsolete cond_check_type_rules() function and call and 
	  cond_optimize_lists() call from checkpolicy.c; these are handled
	  during parsing and expansion now.
	* Updated calls to expand_module for interface change.
	* Changed checkmodule to verify that expand_module succeeds 
	  when building base modules.
	* Merged module compiler fixes from Joshua Brindle.
	* Removed direct calls to hierarchy_check_constraints() and 
	  check_assertions() from checkpolicy since they are now called 
	  internally by expand_module().

* Tue Oct 18 2005 Dan Walsh <dwalsh@redhat.com> 1.27.11-1
- Latest upgrade from NSA
	* Updated for changes to sepol policydb_index_others interface.

* Tue Oct 18 2005 Dan Walsh <dwalsh@redhat.com> 1.27.10-1
- Latest upgrade from NSA
	* Updated for changes to sepol expand_module and link_modules interfaces.
* Sat Oct 15 2005 Dan Walsh <dwalsh@redhat.com> 1.27.9-2
- Rebuild to get latest libsepol

* Fri Oct 14 2005 Dan Walsh <dwalsh@redhat.com> 1.27.9-1
- Latest upgrade from NSA
	* Merged support for require blocks inside conditionals from
	Joshua Brindle (Tresys).

* Wed Oct 12 2005 Karsten Hopp <karsten@redhat.de> 1.27.8-2
- add buildrequirement for libselinux-devel for dispol

* Mon Oct 10 2005 Dan Walsh <dwalsh@redhat.com> 1.27.8-1
- Latest upgrade from NSA
	* Updated for changes to libsepol.

* Fri Oct 7 2005 Dan Walsh <dwalsh@redhat.com> 1.27.7-2
- Rebuild to get latest libsepol

* Thu Oct 6 2005 Dan Walsh <dwalsh@redhat.com> 1.27.7-1
- Latest upgrade from NSA
	* Merged several bug fixes from Joshua Brindle (Tresys).

* Tue Oct 4 2005 Dan Walsh <dwalsh@redhat.com> 1.27.6-1
- Latest upgrade from NSA
	* Merged MLS in modules patch from Joshua Brindle (Tresys).

* Mon Oct 3 2005 Dan Walsh <dwalsh@redhat.com> 1.27.5-2
- Rebuild to get latest libsepol

* Wed Sep 28 2005 Dan Walsh <dwalsh@redhat.com> 1.27.5-1
- Latest upgrade from NSA
	* Merged error handling improvement in checkmodule from Karl MacMillan (Tresys).

* Tue Sep 27 2005 Dan Walsh <dwalsh@redhat.com> 1.27.4-1
- Latest upgrade from NSA
	* Merged bugfix for dup role transition error messages from
	Karl MacMillan (Tresys).

* Fri Sep 23 2005 Dan Walsh <dwalsh@redhat.com> 1.27.3-1
- Latest upgrade from NSA
	* Merged policyver/modulever patches from Joshua Brindle (Tresys).

* Wed Sep 21 2005 Dan Walsh <dwalsh@redhat.com> 1.27.2-2
- Rebuild to get latest libsepol

* Wed Sep 21 2005 Dan Walsh <dwalsh@redhat.com> 1.27.2-1
- Latest upgrade from NSA
	* Fixed parse_categories handling of undefined category.

* Tue Sep 20 2005 Dan Walsh <dwalsh@redhat.com> 1.27.1-2
- Rebuild to get latest libsepol

* Sat Sep 17 2005 Dan Walsh <dwalsh@redhat.com> 1.27.1-1
- Latest upgrade from NSA
	* Merged bug fix for role dominance handling from Darrel Goeddel (TCS). 
* Wed Sep 14 2005 Dan Walsh <dwalsh@redhat.com> 1.26-2
- Rebuild to get latest libsepol

* Mon Sep 12 2005 Dan Walsh <dwalsh@redhat.com> 1.26-1
- Latest upgrade from NSA
	* Updated version for release.
- Rebuild to get latest libsepol

* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 1.25.12-3
- Rebuild to get latest libsepol

* Mon Aug 29 2005 Dan Walsh <dwalsh@redhat.com> 1.25.12-2
- Rebuild to get latest libsepol

* Mon Aug 22 2005 Dan Walsh <dwalsh@redhat.com> 1.25.12-1
- Update to NSA Release
	* Fixed handling of validatetrans constraint expressions.
	Bug reported by Dan Walsh for checkpolicy -M.

* Mon Aug 22 2005 Dan Walsh <dwalsh@redhat.com> 1.25.11-2
- Fix mls crash

* Fri Aug 19 2005 Dan Walsh <dwalsh@redhat.com> 1.25.11-1
- Update to NSA Release
	* Merged use-after-free fix from Serge Hallyn (IBM).  
	  Bug found by Coverity.

* Sun Aug 14 2005 Dan Walsh <dwalsh@redhat.com> 1.25.10-1
- Update to NSA Release
	* Fixed further memory leaks found by valgrind.
	* Changed checkpolicy to destroy the policydbs prior to exit
	  to allow leak detection.
	* Fixed several memory leaks found by valgrind.

* Sun Aug 14 2005 Dan Walsh <dwalsh@redhat.com> 1.25.8-3
- Rebuild to get latest libsepol changes

* Sat Aug 13 2005 Dan Walsh <dwalsh@redhat.com> 1.25.8-2
- Rebuild to get latest libsepol changes

* Thu Aug 11 2005 Dan Walsh <dwalsh@redhat.com> 1.25.8-1
- Update to NSA Release
	* Updated checkpolicy and dispol for the new avtab format.
	  Converted users of ebitmaps to new inline operators.
  	  Note:  The binary policy format version has been incremented to 
	  version 20 as a result of these changes.  To build a policy
	  for a kernel that does not yet include these changes, use
	  the -c 19 option to checkpolicy.
	* Merged patch to prohibit use of "self" as a type name from Jason Tang (Tresys).
	* Merged patch to fix dismod compilation from Joshua Brindle (Tresys).

* Wed Aug 10 2005 Dan Walsh <dwalsh@redhat.com> 1.25.5-1
- Update to NSA Release
	* Fixed call to hierarchy checking code to pass the right policydb.
	* Merged patch to update dismod for the relocation of the
	  module read/write code from libsemanage to libsepol, and
	  to enable build of test subdirectory from Jason Tang (Tresys).

* Thu Jul 28 2005 Dan Walsh <dwalsh@redhat.com> 1.25.3-1
- Update to NSA Release
	* Merged hierarchy check fix from Joshua Brindle (Tresys).

* Thu Jul 7 2005 Dan Walsh <dwalsh@redhat.com> 1.25.2-1
- Update to NSA Release
	* Merged loadable module support from Tresys Technology.
	* Merged patch to prohibit the use of * and ~ in type sets 
	  (other than in neverallow statements) and in role sets
	  from Joshua Brindle (Tresys).
	* Updated version for release.

* Fri May 20 2005 Dan Walsh <dwalsh@redhat.com> 1.23-4-1
- Update to NSA Release
	* Merged cleanup patch from Dan Walsh.

* Thu May 19 2005 Dan Walsh <dwalsh@redhat.com> 1.23-3-1
- Update to NSA Release
	* Added sepol_ prefix to Flask types to avoid namespace
	  collision with libselinux.

* Fri May 7 2005 Dan Walsh <dwalsh@redhat.com> 1.23-2-1
- Update to NSA Release
	* Merged identifier fix from Joshua Brindle (Tresys).

* Thu Apr 14 2005 Dan Walsh <dwalsh@redhat.com> 1.23,1-1
	* Merged hierarchical type/role patch from Tresys Technology.
	* Merged MLS fixes from Darrel Goeddel of TCS.

* Thu Mar 10 2005 Dan Walsh <dwalsh@redhat.com> 1.22-1
- Update to NSA Release

* Tue Mar 1 2005 Dan Walsh <dwalsh@redhat.com> 1.21.4-2
- Rebuild for FC4

* Thu Feb 17 2005 Dan Walsh <dwalsh@redhat.com> 1.21.4-1
	* Merged define_user() cleanup patch from Darrel Goeddel (TCS).
	* Moved genpolusers utility to libsepol.
	* Merged range_transition support from Darrel Goeddel (TCS).

* Thu Feb 10 2005 Dan Walsh <dwalsh@redhat.com> 1.21.2-1
- Latest from NSA
	* Changed relabel Makefile target to use restorecon.

* Mon Feb 7 2005 Dan Walsh <dwalsh@redhat.com> 1.21.1-1
- Latest from NSA
	* Merged enhanced MLS support from Darrel Goeddel (TCS).

* Fri Jan 7 2005 Dan Walsh <dwalsh@redhat.com> 1.20.1-1
- Update for version increase at NSA

* Mon Dec 20 2004 Dan Walsh <dwalsh@redhat.com> 1.19.2-1
- Latest from NSA
	* Merged typeattribute statement patch from Darrel Goeddel of TCS.
	* Changed genpolusers to handle multiple user config files.
	* Merged nodecon ordering patch from Chad Hanson of TCS.

* Thu Nov 11 2004 Dan Walsh <dwalsh@redhat.com> 1.19.1-1
- Latest from NSA
	* Merged nodecon ordering patch from Chad Hanson of TCS.

* Thu Nov 4 2004 Dan Walsh <dwalsh@redhat.com> 1.18.1-1
- Latest from NSA
	* MLS build fix.

* Sat Sep 4 2004 Dan Walsh <dwalsh@redhat.com> 1.17.5-1
- Latest from NSA
	* Fixed Makefile dependencies (Chris PeBenito).

* Sat Sep 4 2004 Dan Walsh <dwalsh@redhat.com> 1.17.4-1
- Latest from NSA
	* Fixed Makefile dependencies (Chris PeBenito).

* Sat Sep 4 2004 Dan Walsh <dwalsh@redhat.com> 1.17.3-1
- Latest from NSA
	* Merged fix for role dominance ordering issue from Chad Hanson of TCS.

* Mon Aug 30 2004 Dan Walsh <dwalsh@redhat.com> 1.17.2-1
- Latest from NSA

* Thu Aug 26 2004 Dan Walsh <dwalsh@redhat.com> 1.16.3-1
- Fix NSA package to not include y.tab files.

* Tue Aug 24 2004 Dan Walsh <dwalsh@redhat.com> 1.16.2-1
- Latest from NSA
- Allow port ranges to overlap

* Sun Aug 22 2004 Dan Walsh <dwalsh@redhat.com> 1.16.1-1
- Latest from NSA

* Mon Aug 16 2004 Dan Walsh <dwalsh@redhat.com> 1.15.6-1
- Latest from NSA

* Fri Aug 13 2004 Dan Walsh <dwalsh@redhat.com> 1.15.5-1
- Latest from NSA

* Wed Aug 11 2004 Dan Walsh <dwalsh@redhat.com> 1.15.4-1
- Latest from NSA

* Sat Aug 8 2004 Dan Walsh <dwalsh@redhat.com> 1.15.3-1
- Latest from NSA

* Wed Aug 4 2004 Dan Walsh <dwalsh@redhat.com> 1.15.2-1
- Latest from NSA

* Sat Jul 31 2004 Dan Walsh <dwalsh@redhat.com> 1.15.1-1
- Latest from NSA

* Tue Jul 27 2004 Dan Walsh <dwalsh@redhat.com> 1.14.2-1
- Latest from NSA

* Wed Jun 30 2004 Dan Walsh <dwalsh@redhat.com> 1.14.1-1
- Latest from NSA

* Fri Jun 18 2004 Dan Walsh <dwalsh@redhat.com> 1.12.2-1
- Latest from NSA

* Thu Jun 17 2004 Dan Walsh <dwalsh@redhat.com> 1.12.1-1
- Update to latest from NSA

* Wed Jun 16 2004 Dan Walsh <dwalsh@redhat.com> 1.12-1
- Update to latest from NSA

* Wed Jun 16 2004 Dan Walsh <dwalsh@redhat.com> 1.10-5
- Add nlclass patch

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun 4 2004 Dan Walsh <dwalsh@redhat.com> 1.10-3
- Add BuildRequires flex

* Thu Apr 8 2004 Dan Walsh <dwalsh@redhat.com> 1.10-2
- Add BuildRequires byacc

* Thu Apr 8 2004 Dan Walsh <dwalsh@redhat.com> 1.10-1
- Upgrade to the latest from NSA

* Mon Mar 15 2004 Dan Walsh <dwalsh@redhat.com> 1.8-1
- Upgrade to the latest from NSA

* Mon Feb 24 2004 Dan Walsh <dwalsh@redhat.com> 1.6-1
- Upgrade to the latest from NSA

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 20 2004 Dan Walsh <dwalsh@redhat.com> 1.4-6
- Add typealias patch

* Tue Jan 20 2004 Dan Walsh <dwalsh@redhat.com> 1.4-5
- Update excludetypes with negset-final patch

* Wed Jan 14 2004 Dan Walsh <dwalsh@redhat.com> 1.4-4
- Add excludetypes patch

* Wed Jan 14 2004 Dan Walsh <dwalsh@redhat.com> 1.4-3
- Add Colin Walter's lineno patch

* Wed Jan 7 2004 Dan Walsh <dwalsh@redhat.com> 1.4-2
- Remove check for roles transition

* Sat Dec 6 2003 Dan Walsh <dwalsh@redhat.com> 1.4-1
- upgrade to 1.4

* Wed Oct 1 2003 Dan Walsh <dwalsh@redhat.com> 1.2-1
- upgrade to 1.2

* Thu Aug 28 2003 Dan Walsh <dwalsh@redhat.com> 1.1-2
- upgrade to 1.1

* Mon Jun 2 2003 Dan Walsh <dwalsh@redhat.com> 1.0-1
- Initial version

