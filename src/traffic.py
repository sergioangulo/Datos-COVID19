'''
MIT License

Copyright (c) 2020 MINCIENCIA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import json
from urllib import request
import sys
import pandas as pd
from datetime import datetime

class traffic:
    def __init__(self, user, token,new_relic_user,new_relic_key):

        self.user = user
        self.token = token
        self.new_relic_user = new_relic_user
        self.new_relic_key = new_relic_key
        self.df_clones = pd.DataFrame(columns=['timestamp','count','uniques'])
        self.df_views = pd.DataFrame(columns=['timestamp','count','uniques'])
        self.now = pd.to_datetime(datetime.now()).strftime('%Y-%m-%d-%H:%M:%S')


    def lambda_handler(self):
        base_url = "https://api.github.com"
        user = self.user
        print("Getting repositories for %s" % user)
        req = request.Request(
            "%s/users/%s/repos" % (base_url, user), headers={"Authorization": "token %s" % self.token}
        )
        response = request.urlopen(req)
        req = json.load(response)
        ur = [(r["name"]) for r in req]
        print("Found %s repositories" % len(ur))

        print(" ")

        for repo_name in ur:

            print("Getting views for %s" % repo_name)
            req = request.Request(
                "%s/repos/%s/%s/traffic/views" % (base_url, user, repo_name), headers={"Authorization": "token %s" % self.token}
            )
            response = request.urlopen(req)
            req = json.load(response)
            for i in req['views']:
                dfi = pd.Series(i)
                print(dfi)
                self.df_views = self.df_views.append(dfi,ignore_index=True)


            print("Getting clones for %s" % repo_name)
            req = request.Request(
                "%s/repos/%s/%s/traffic/clones" % (base_url, user, repo_name), headers={"Authorization": "token %s" % self.token}
            )
            response = request.urlopen(req)
            req = json.load(response)
            for i in req['clones']:
                dfi = pd.Series(i)
                print(dfi)
                self.df_clones = self.df_clones.append(dfi,ignore_index=True)

            # print("Getting referral data for %s" % repo_name)
            # referrals = request.Request(
            #     "%s/repos/%s/%s/traffic/popular/referrers" % (base_url, user, repo_name), headers={"Authorization": "token %s" % self.token}
            # )
            # referrals = request.urlopen(referrals)
            # referrals = json.load(referrals)
            # if len(referrals) > 0:
            #     for ref in referrals:
            #         referred = {
            #             "eventType": "Referral",
            #             "repo_name": repo_name,
            #             "referrer": ref["referrer"],
            #             "count": ref["count"],
            #             "uniques": ref["uniques"],
            #         }
            #         print(referred)
            #         headers = {
            #             "X-Insert-Key": "%s" % self.new_relic_key,
            #         }
            #         req = request.Request(
            #             "https://insights-collector.newrelic.com/v1/accounts/%s/events"
            #             % self.new_relic_user,
            #             headers=headers,
            #             data=json.dumps(referred).encode("utf-8"),
            #         )
            #         resp = request.urlopen(req)
            #         print(resp.read())
            #
            # print("Getting top referral path data for %s" % repo_name)
            #
            # paths = request.Request(
            #     "%s/repos/%s/%s/traffic/popular/paths" % (base_url, user, repo_name), headers={"Authorization": "token %s" % self.token}
            # )
            # paths = request.urlopen(paths)
            # paths = json.load(paths)
            # if len(paths) > 0:
            #     for ref in paths:
            #         paths = {
            #             "eventType": "ReferralPath",
            #             "repo_name": repo_name,
            #             "path": ref["path"],
            #             "title": ref["title"],
            #             "count": ref["count"],
            #             "uniques": ref["uniques"],
            #         }
            #         print(paths)
            #         headers = {
            #             "X-Insert-Key": "%s" % self.new_relic_key,
            #         }
            #         req = request.Request(
            #             "https://insights-collector.newrelic.com/v1/accounts/%s/events"
            #             % self.new_relic_user,
            #             headers=headers,
            #             data=json.dumps(paths).encode("utf-8"),
            #         )
            #         resp = request.urlopen(req)
            #         print(resp.read())
            #

    def save(self):
        #views
        self.df_views['timestamp'] = pd.to_datetime(self.df_views['timestamp'], format='%Y-%m-%d').dt.date
        self.df_views.to_csv('../input/traffic/%s_views.csv' % self.now,index=False)

        #clones
        self.df_clones['timestamp'] = pd.to_datetime(self.df_clones['timestamp'], format='%Y-%m-%d').dt.date
        self.df_clones.to_csv('../input/traffic/%s_clones.csv' % self.now,index=False)

if __name__ == '__main__':
    my_user = sys.argv[2]
    my_token = sys.argv[1]
    my_newrelic_user = sys.argv[3]
    my_newrelic_key = sys.argv[4]
    my_traffic = traffic(my_user,my_token,my_newrelic_user,my_newrelic_key)
    my_traffic.lambda_handler()
    my_traffic.save()


