        $(function(){
           var nutrition = ["calories",
                            "carbohydrate",
                            "proteins",
                            "fat",
                            "dietary_fiber",
                            "sodium",
                            "sodium_chloride_equivalent",
                            "potassium",
                            "calcium",
                            "iron",
                            "magnesium",
                            "phosphorus",
                            "vitamin_A",
                            "vitamin_B1",
                            "vitamin_B2",
                            "vitamin_B6",
                            "vitamin_B12",
                            "niacin",
                            "vitamin_C",
                            "vitamin_D",
                            "vitamin_E"];


   // Handle drag and drop events with jQuery
          var obj = $("#dragandrophandler");
          obj.on('dragenter', function (e)
          {
              e.stopPropagation();
              e.preventDefault();
              $(this).css('border', '2px solid #0B85A1');
          });
          obj.on('dragover', function (e)
          {
               e.stopPropagation();
               e.preventDefault();
          });
          obj.on('drop', function (e)
          {
               console.log('test');

               $(this).css('border', '2px dotted #0B85A1');
               e.preventDefault();

               // ドラッグドロップされたファイルのオブジェクト
               var files = e.originalEvent.dataTransfer.files;
               console.log(files);

               showFileContents(files,obj);
          });



   // prevent ‘drop’ event on other place of the browser window
         $(document).on('dragenter', function (e)
         {
             e.stopPropagation();
             e.preventDefault();
         });
         $(document).on('dragover', function (e)
         {
           e.stopPropagation();
           e.preventDefault();
           obj.css('border', '2px dotted #0B85A1');
         });
         $(document).on('drop', function (e)
         {
             e.stopPropagation();
             e.preventDefault();
         });



   // Read the file contents using HTML5 FormData() when the files are dropped.
         function showFileContents(files,obj)
         {
            var s;

            for (var i = 0; i < files.length; i++){
                 var fd = new FormData();
                 fd.append('file', files[i]);
                 s += '<tr><td>ファイル名</td><td>' + files[i].name + '</td></tr>';
                 sendFileToServer(fd)
            }
//            console.log(fd.length)

           $('.showFileName').append(s);
         }


         //送信
         function sendFileToServer(formData){
           $('#submitBtn').on('click', function(e){ //送信ボタンが押されたら
                 e.preventDefault();
                 var gender = $('#thisForm [name=gender]').val()
                 console.log(gender)
//                       console.log(formData);

                 // サーバーに送る　→　サーバーからの出力表示
//                 var path = 'http://localhost:8080/upload/' + fName;
//                 console.log(path);

                 $.ajax({
                     method: 'post',
                     url: '/upload',　//(ここには処理系を書く(ふつうはphpだけど、今回はpython))
                     dataType: 'json',
                     data: formData, //　送る画像のパス
                     processData: false,
                     contentType: false

                 }).done(function (res) {
                     console.log('done');
                     var percent = res.per_dict// 成功した場合、レスポンスからデータを取り出します。
                     var real_value = res.real_value
                     console.log(res.food_name)

                     var bargraph_color = ['#000000',
                         '#808080',
                         '#C0C0C0C0',
                         '#CCFFFF',
                         '#0000ff',
                         '#00FFFF',
                         '#008000',
                         '#00ff00',
                         '#FFFF00',
                         '#800080',
                         '#ff00ff',
                         '#FF0000',
                         '#98fb98',
                         '#90ee90',
                         '#adff2f',
                         '#7fff00',
                         '#7cfc00',
                         '#00ff7f',
                         '#00fa9a',
                         '#7fffd4',
                         '#40e0d0'
                       ];

                     new Chart(document.getElementById("myChart_1"), { //横にしているから軸は逆
                         type: "horizontalBar",
                         data: {
                           labels: nutrition,
                           datasets: [{
                             data: [percent.calories,
                                    percent.carbohydrate,
                                    percent.proteins,
                                    percent.fat,
                                    percent.dietary_fiber,
                                    percent.sodium,
                                    percent.sodium_chloride_equivalent,
                                    percent.potassium,
                                    percent.calcium,
                                    percent.iron,
                                    percent.magnesium,
                                    percent.phosphorus,
                                    percent.vitamin_A,
                                    percent.vitamin_B1,
                                    percent.vitamin_B2,
                                    percent.vitamin_B6,
                                    percent.vitamin_B12,
                                    percent.niacin,
                                    percent.vitamin_C,
                                    percent.vitamin_D,
                                    percent.vitamin_E
                                  ],
                             backgroundColor: bargraph_color
                           }]
                         },
                         options:{
                           responsive: true,
                           legend: {
                             display: false
                           },
                           title: {                         //タイトル設定
                             display: true,                 //表示設定
                             fontSize: 30,                  //フォントサイズ
                             text: 'ALL NUTRITION'                //ラベル
                           },
                           scales:{
                             yAxes:[{
                               display: true,                //表示設定
                               barPercentage: 1.0,           //棒グラフ幅
                               categoryPercentage: 1.0,      //棒グラフ幅
                               scaleLabel: {                 //軸ラベル設定
                                 display:false,             //表示設定
                                 labelString: '',  //ラベル
                                 fontSize: 18
                               }              //フォントサイズ
                             }],
                             xAxes: [{
                               display: true,
                               ticks: { //軸設定
                                 min: 0,
                                 max: 120,
                                 fontSize: 20,
                                 stepSize:5
                               }
                             }]
                            }
                          }
                     });

                     new Chart(document.getElementById("myChart_2"), {
                         type: 'radar',
                         data: {
                            labels: ["protains", "salt", "energe", "lipid", "carbohydrate", "iron", "vitaminC"],
                            datasets: [{
                              label: 'Main Nutrition',
                              borderColor: "#ccffcc",
                              borderColor: "#00FF00",
                              data: [percent.protains, percent.sodium_chloride_equivalent, percent.calories, percent.fat, percent.carbohydrate, percent.iron, percent.vitamin_C]
                            },{
                              label: 'Reference Value',
                              borderColor: "#C0C0C0",
                              data: [100, 100, 100, 100, 100, 100, 100]
                            }]
                         },
                         options:{
                           responsive: true,
                           legend: {
                             display: true
                           },
                           title: {
                             display: true,
                             fontSize: 30,
                             text: 'MAIN NUTRITION'
                           },
                           scale: {
                             display: true,
                             pointLabels: {
                              fontSize: 15,
                            },
                            ticks: {
                              display: true,
                              fontSize: 12,
                              fontColor: "#000000",
                                min: 0,
                                max: 120,
                                beginAtZero: true
                            }
                           }
                          }
                     });



                     $("#food").html( "<font size='5' color='mediumseagreen'><b>"+ res.food_name +"</b></font>, aren't you?");

                   	 $("#out1").html('<td>calories：</td><td>'+ real_value.calories +' kcal</td>');
                   	 $("#out2").html('<td>carbohydrate：</td><td>'+ real_value.carbohydrate +' g</td>');
                   	 $("#out3").html('<td>proteins：</td><td>'+ real_value.proteins +' g</td>');
                   	 $("#out4").html('<td>fat :</td><td>'+ real_value.fat +' g</td>');
                     $("#out5").html('<td>dietary_fiber :</td><td>'+ real_value.dietary_fiber +' g</td>');
                     $("#out6").html('<td>sodium :</td><td>'+ real_value.sodium +' mg</td>');
                     $("#out7").html('<td>sodium_chloride_equivalent :</td><td>'+ real_value.sodium_chloride_equivalent +' g</td>');
                     $("#out8").html('<td>potassium :</td><td>'+ real_value.potassium +' mg</td>');
                     $("#out9").html('<td>calcium :</td><td>'+ real_value.calcium +' mg</td>');
                     $("#out10").html('<td>iron :</td><td>'+ real_value.iron +' mg</td>');
                     $("#out11").html('<td>magnesium :</td><td>'+ real_value.magnesium +' mg</td>');
                     $("#out12").html('<td>phosphorus :</td><td>'+ real_value.phosphorus +' mg</td>');
                     $("#out13").html('<td>vitamin_A :</td><td>'+ real_value.vitamin_A +' μg</td>');
                     $("#out14").html('<td>vitamin_B1 :</td><td>'+ real_value.vitamin_B1 +' mg</td>');
                     $("#out15").html('<td>vitamin_B2 :</td><td>'+ real_value.vitamin_B2 +' mg</td>');
                     $("#out16").html('<td>vitamin_B6 :</td><td>'+ real_value.vitamin_B6 +' mg</td>');
                     $("#out17").html('<td>vitamin_B12 :</td><td>'+ real_value.vitamin_B12 +' μg</td>');
                     $("#out18").html('<td>niacin :</td><td>'+ real_value.niacin +' mg</td>');
                     $("#out19").html('<td>vitamin_C :</td><td>'+ real_value.vitamin_C +' mg</td>');
                     $("#out20").html('<td>vitamin_D :</td><td>'+ real_value.vitamin_D +' μg</td>');
                     $("#out21").html('<td>vitamin_E :</td><td>'+ real_value.vitamin_E +' mg</td>');

                     $("#radar_chart").append('<img src='+res.radar_chart_path+' alt="radar chart">');

                     $("#recommend_menu").append("I recommend you to eat   <font size='5' color='mediumseagreen'><b>"+res.recommend_menu+"</b></font>");
                     $("#recommend_photo").append('<img src='+res.recommend_imd_path+' alt="recommend">');


                 }).fail(function(data) {
                     console.log('fail')
                 })
               });
         }
     });

