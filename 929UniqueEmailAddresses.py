class Solution:
	def numUniqueEmails(self, emails):
		isemail = set()
		for email in emails:
		    not_local_name, domain_name = email.split('@')
		    local_name = ''.join(not_local_name.split('+')[0].split('.'))
		    real_email = local_name + '@' + domain_name
		    isemail.add(real_email)
		    re = len(isemail)
		return re


def main():
	s = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	ret = Solution().numUniqueEmails(s)
	out = (ret);
	print(out)

if __name__ == '__main__':
	main()