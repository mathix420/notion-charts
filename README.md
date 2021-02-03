# notion-charts

![image](docs/example.png)

<details>
  <summary>See other examples</summary>
  
  ### Business Dashboard
  ![Business Dashboard](https://i.redd.it/9i9pkp1wbvp41.png)

  ### Dev Dashboard
  ![Dev Dashboard](docs/example2.png)
  
</details>

## Usage

### For public notions

Simply use https://charts.mathix.ninja url, and follow the documentation below.

### For private notions

You'll need to host your own version of this repository.
The best way to do that is by clicking this button below, it will automatically host this API on [vercel.com](https://vercel.com/) which is **100% free**.

<details>
  <summary>Show me the steps</summary>

  1. Click the blue **Deploy** button on this page
  2. Log in or sign up to continue.
  3. Choose a name for your project, keep in mind that this name will goes in your url `https://YOUR-PROJECT-NAME.now.sh`
  4. Follow instructions and don't forget to put your notion `TOKEN_V2` before clicking **Continue** [If you don't know how to get it, click here](/docs/notion-token.md)
  5. Click **Continue** one more time, and you're done!

</details>

Then when the hosting is completed simply follow documentation instructions below and enjoy 😎 
Don't forget to use your URL instead of `charts.mathix.ninja`.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2Fmathix420%2Fnotion-charts.git&env=TOKEN_V2&envDescription=Notion%20session%20cookie&envLink=https%3A%2F%2Fgithub.com%2Fmathix420%2Fnotion-charts%2Fblob%2Fmaster%2Fdocs%2Fnotion-token.md)

If you want to stay up to date I will recommend you to use a [Deploy Hook](https://vercel.com/docs/v2/more/deploy-hooks).

## Documentation

For fast and easy previews you can now [go directly here](https://charts.mathix.ninja).

### Split notion url

> https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> collection_id = fa9b093633c0479f886fdb857f57f9b0
>
> view_id = c94a0043c3df410cb461e7698cee6aff

### Image charts

```
/chart-image/<collection>/<view>
```
Example:

> Inital page => https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> Chart => https://charts.mathix.ninja/chart-image/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff

Simply paste the chart url in your notion and click **Embbed**

### Interactive charts

```
/chart/<collection>/<view>
```
Examples:

> Inital page => https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> Chart => https://charts.mathix.ninja/chart/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff


> Inital page => https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=f1b7adb289cc4da3aa7ee6b8ac68470e
>
> Chart => https://charts.mathix.ninja/chart/fa9b093633c0479f886fdb857f57f9b0/f1b7adb289cc4da3aa7ee6b8ac68470e


### Custom status

You can use custom columns name with the `l` parameter

```
/chart-image/<collection>/<view>?l=<NAME1>|<NAME2>|...|<END-NAME>
/chart/<collection>/<view>?l=<NAME1>|<NAME2>|...|<END-NAME>
```

Example:

> Inital page => https://www.notion.so/049c3ee811c344868b78d043e152241b?v=376b00ef4b634a7f9b51ee78bc361e15
>
> Chart => https://charts.mathix.ninja/chart/049c3ee811c344868b78d043e152241b/376b00ef4b634a7f9b51ee78bc361e15?l=Next%20Up|In%20Progress|Completed


### Dark-mode

Dark-mode is only available for interactive charts.

```
/chart/<collection>/<view>?dark
```

Examples:
> https://charts.mathix.ninja/chart/049c3ee811c344868b78d043e152241b/376b00ef4b634a7f9b51ee78bc361e15?l=Next%20Up|In%20Progress|Completed&dark
>
> https://charts.mathix.ninja/chart/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff?dark


## Open for contributions

I know this API is not very flexible, but if someone want to make it better
I'd be glad to accept its contribution.
