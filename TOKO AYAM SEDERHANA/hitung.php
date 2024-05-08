<?php
$totalsemua = @$_POST['total'];
$bilangan1 = @$_POST['total-belanja'];
$bilangan2 = @$_POST['uang'];

$hasil=$bilangan2-$bilangan1;

?>




<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PEMBAYARAN</title>
    <link rel="stylesheet" href="style2.css">
</head>
<body>
    <div class="wraper">
        <form action="" method="post">
            <h1>Total Pesanan Anda</h1>
            <div class="input-box">
                <p>Total pembayaran anda <?php echo $totalsemua ?></p>
                <br>
                <input type="text" name='total-belanja' placeholder="Masukan Jumlah Pembelian Anda">
            </div>
            <br>
            <br>
            <div class="input-box">
                <input type="text" name='uang' placeholder="Masukan Uang Anda">
            </div>
            <button type="submit" class="btn">Bayar</button>   
            <div class="input-box">
                <input type="text" placeholder="hasil"  value= <?php echo number_format($hasil, 2, ",", ".");?>>
                <p>SISA UANG KAMU ADALAH <?php  echo number_format($hasil, 2, ",", ".");?></p>
            </div>
        </form>
    </div>
</body>
</html>
