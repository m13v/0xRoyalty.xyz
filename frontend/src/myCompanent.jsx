import React, { useState, useEffect } from "react";
//import data table design
// import { DataGrid } from '@mui/x-data-grid';
import { alpha, styled } from '@mui/material/styles';
import { DataGrid, gridClasses } from '@mui/x-data-grid';
// import { createTheme, ThemeProvider } from '@mui/material/styles';

// const theme = createTheme({
//   components: {
//     // Name of the component
//     MuiDataGrid: {
//       defaultProps: {
//         // The props to change the default for.
//         whiteSpace: normal, // text wrapping
//       },
//     },
//   },
// });

const ODD_OPACITY = 0.2;

const StripedDataGrid = styled(DataGrid)(({ theme }) => ({
  [`& .${gridClasses.row}.even`]: {
    backgroundColor: theme.palette.grey[200],
    '&:hover, &.Mui-hovered': {
      backgroundColor: alpha(theme.palette.primary.main, ODD_OPACITY),
      '@media (hover: none)': {
        backgroundColor: 'transparent',
      },
    },
    '&.Mui-selected': {
      backgroundColor: alpha(
        theme.palette.primary.main,
        ODD_OPACITY + theme.palette.action.selectedOpacity,
      ),
      '&:hover, &.Mui-hovered': {
        backgroundColor: alpha(
          theme.palette.primary.main,
          ODD_OPACITY +
            theme.palette.action.selectedOpacity +
            theme.palette.action.hoverOpacity,
        ),
        // Reset on touch devices, it doesn't add specificity
        '@media (hover: none)': {
          backgroundColor: alpha(
            theme.palette.primary.main,
            ODD_OPACITY + theme.palette.action.selectedOpacity,
          ),
        },
      },
    },
  },
}));

const columns = [
  { field: 'id', headerName: '#Rank', width: 70 },
  { field: 'username', headerName: 'Github username', width: 130 },
  { 
    field: 'protocol',  
    headerName: "Protocol they contributed to", 
    width: 130 },
  {
    field: 'sh_commit',
    headerName: 'Share of repo commit',
//    type: 'number',    width: 90,
  },
  {
    field: 'volume',
    headerName: 'Protocol Volume 1y',
//    type: 'number',
    width: 90,
  },
  {
    field: 'weight',
    headerName: 'Protocol weight in overall results',
//    type: 'number',
    width: 110,
  },
  {
    field: 'score',
    headerName: 'Developer score',
//    type: 'number',
    width: 90,
  },
  {
    field: 'commits',
    headerName: 'Total number of commits',
//    type: 'number',
    width: 90,
  },
  {
    field: 'merges',
    headerName: 'Total number of merges',
//    type: 'number',
    width: 90,
  },
  // {
  //   field: 'fullName',
  //   headerName: 'Full name',
  //   description: 'This column has a value getter and is not sortable.',
  //   sortable: false,
  //   width: 160,
  //   valueGetter: (params) =>
  //     `${params.row.firstName || ''} ${params.row.lastName || ''}`,
  // },
];

const rows = [
  { id: 1, username: '[link to github profile]', protocol: '[link to github repo]', sh_commit: 35 },
  { id: 2, username: 'Lannister', protocol: 'Cersei', sh_commit: 42 },
  { id: 3, username: 'Lannister', protocol: 'Jaime', sh_commit: 45 },
  { id: 4, username: 'Stark', protocol: 'Arya', sh_commit: 16 },
  { id: 5, username: 'Targaryen', protocol: 'Daenerys', sh_commit: null },
  { id: 6, username: 'Melisandre', protocol: null, sh_commit: 150 },
  { id: 7, username: 'Clifford', protocol: 'Ferrara', sh_commit: 44 },
  { id: 8, username: 'Frances', protocol: 'Rossini', sh_commit: 36 },
  { id: 9, username: 'Roxie', protocol: 'Harvey', sh_commit: 65 },
];


export default class myCompanent extends React.Component {
  constructor(props){
    super(props)
    console.log(this.state)
  }
  
  render(){
    return (
    <div style={{ height: 400, width: 902 }}>
      { /*<ThemeProvider theme={theme}> */}
        <StripedDataGrid
          rows={rows}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
          getRowClassName={(params) =>
          params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
          }
          //checkboxSelection
        />
      {/*</ThemeProvider>*/}
    </div>
    )
  }
  
}