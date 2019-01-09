apt-get install git nano

apt-get install apache2 mysql-server libappconfig-perl libdate-calc-perl libtemplate-perl libmime-perl build-essential libdatetime-timezone-perl libdatetime-perl libemail-sender-perl libemail-mime-perl libemail-mime-modifier-perl libdbi-perl libdbd-mysql-perl libcgi-pm-perl libmath-random-isaac-perl libmath-random-isaac-xs-perl libapache2-mod-perl2 libapache2-mod-perl2-dev libchart-perl libxml-perl libxml-twig-perl perlmagick libgd-graph-perl libtemplate-plugin-gd-perl libsoap-lite-perl libhtml-scrubber-perl libjson-rpc-perl libdaemon-generic-perl libtheschwartz-perl libtest-taint-perl libauthen-radius-perl libfile-slurp-perl libencode-detect-perl libmodule-build-perl libnet-ldap-perl libauthen-sasl-perl libtemplate-perl-doc libfile-mimeinfo-perl libhtml-formattext-withlinks-perl libgd-dev libmysqlclient-dev lynx-cur graphviz python-sphinx


git clone --branch release-5.0.4 https://github.com/bugzilla/bugzilla

<Directory /var/live_code/bugzilla>
  AddHandler cgi-script .cgi
  Options +ExecCGI +FollowSymLinks
  DirectoryIndex index.cgi index.html
  AllowOverride All
</Directory>


GRANT SELECT, INSERT,
UPDATE, DELETE, INDEX, ALTER, CREATE, LOCK TABLES,
CREATE TEMPORARY TABLES, DROP, REFERENCES ON bugs.*
TO bugs@localhost IDENTIFIED BY 'bugzilla';

FLUSH PRIVILEGES;

<VirtualHost *:80>
  ServerName localhost
  DocumentRoot /var/live_code/bugzilla

  <Directory "/var/live_code/phabricator/bugzilla">
	AddHandler cgi-script .cgi
	Options +ExecCGI
	DirectoryIndex index.cgi index.html
	AllowOverride All
  </Directory>

  ErrorLog /var/log/bugzilla/error.log
  CustomLog /var/log/bugzilla/access.log combined
</VirtualHost>

ServerName localhost

<Directory /var/www/html/bugzilla>
  
</Directory>


bdabb maaaz ankit 
ADMIN_MEDIA_PREFIXaaadaa
cczc
dsdsfmnn
echo "# git-bug-repo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add test-bug git@github.com:string-maaz/git-bug-repo.git
git push -u origin master


[/Users/maaz/Downloads/bugzillahook/.git]
bugzilla_url: https://bugzilla.string.org.in/
bugzilla_user: maaz.azmi@string.org.in
bugzilla_password: azmi@4871
allowed_bug_states: NEW, ASSIGNED, REOPENED
os.environ["DEBUSSY"] = "1"

os.environ["GHBH_BUGZILLA_URL"]="https://bugzilla.string.org.in/xmlrpc.cgi"
os.environ["GHBH_BUGZILLA_USERNAME"]="maaz.azmi"
os.environ["GHBH_BUGZILLA_PASSWORD"]="azmi@4871"

for each_page in Pages.objects.all():
	if not each_page.is_active:
		sugg_objs = SuggestionPage.objects.filter(page = each_page)
		if sugg_objs:
			for each_obj in sugg_objs:
				if each_obj.is_active:
					print("inactivating",each_page.name)
					each_obj.is_active = False
					each_obj.save()

for each_user in User.objects.filter(is_active=True):
	all_follow = Follower.objects.filter(user_follower = each_user,is_active = True, is_archived = False).values_list("user_following",flat=True)
	sugg_user = SuggestionUser.objects.filter(for_user = each_user,is_active = True)
	for each_sugg_obj in sugg_user:
		if each_sugg_obj.sugg_user_id in all_follow:
			print("inactivting suggestion",each_user,each_sugg_obj.sugg_user)
			each_sugg_obj.is_active=False
			each_sugg_obj.save()












