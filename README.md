# notion-charts

![image](/example.png)

<details>
  <summary>See other examples</summary>
  
  ### Business Dashboard
  ![Business Dashboard](https://i.redd.it/9i9pkp1wbvp41.png)
  
</details>

## Usage

### For public notions

Simply use https://notion-charts.now.sh url, and follow the documentation below.

### For private notions

You'll need to host your own version of this repository.
The best way to do that is by clicking this button below, it will automatically host this API on [zeit.co](https://zeit.co/) which is **100% free**.

<details>
  <summary>Show me the steps</summary>

  1. Click the blue **Deploy** button on this page
  2. Zeit is now opened, click **Continue**
  2. Then if you don't already have an account click **Sign Up** in the top right corner
  3. Choose a name for your project, keep in mind that this name will goes in your url `https://YOUR-PROJECT-NAME.now.sh`
  4. Don't forget to put your notion `TOKEN_V2` before clicking **Continue** [If you don't know how to get it, click here](/docs/notion-token.md)
  5. Click **Continue** one more time, and you're done!

</details>

Then when the hosting is completed simply follow documentation instructions below and enjoy 😎
Don't forget to use your URL instead of `notion-charts.now.sh`.

[![Deploy with ZEIT Now](https://zeit.co/button)](https://zeit.co/import/project?template=https://github.com/mathix420/notion-charts)


## Documentation

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
> Chart => https://notion-charts.now.sh/chart-image/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff

Simply paste the chart url in your notion and click **Embbed**

### Interactive charts

```
/chart/<collection>/<view>
```
Examples:

> Inital page => https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> Chart => https://notion-charts.now.sh/chart/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff


> Inital page => https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=f1b7adb289cc4da3aa7ee6b8ac68470e
>
> Chart => https://notion-charts.now.sh/chart/fa9b093633c0479f886fdb857f57f9b0/f1b7adb289cc4da3aa7ee6b8ac68470e


### Custom status

You can use custom columns name with the `l` parameter

```
/chart-image/<collection>/<view>?l=<NAME1>|<NAME2>|...|<END-NAME>
/chart/<collection>/<view>?l=<NAME1>|<NAME2>|...|<END-NAME>
```

Example:

> Inital page => https://www.notion.so/049c3ee811c344868b78d043e152241b?v=376b00ef4b634a7f9b51ee78bc361e15
>
> Chart => https://notion-charts.now.sh/chart/049c3ee811c344868b78d043e152241b/376b00ef4b634a7f9b51ee78bc361e15?l=Next%20Up|In%20Progress|Completed


### Dark-mode

Dark-mode is only available for interactive charts.

```
/chart/<collection>/<view>?dark
```

Examples:
> https://notion-charts.now.sh/chart/049c3ee811c344868b78d043e152241b/376b00ef4b634a7f9b51ee78bc361e15?l=Next%20Up|In%20Progress|Completed&dark
>
> https://notion-charts.now.sh/chart/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff?dark


## Open for contributions

I know this API is not very flexible, but if someone want to make it better
I'd be glad to accept its contribution.
