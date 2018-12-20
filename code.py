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


bdabb


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